# -*- coding: utf-8 -*-
# Copyright (C) 2013-2015 Samuel Damashek, Peter Foley, James Forcier, Srijay Kasturi, Reed Koser, Christopher Reffett, and Fox Wilson
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA.

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from time import time
from .orm import setup_db, Log


def get_session(config):
    if not config['db']['engine']:
        raise Exception("You must specify a valid sqlalchemy url in the db.engine config option.")
    engine = create_engine(config['db']['engine'])
    return sessionmaker(bind=engine)


class Sql():

    def __init__(self, config, confdir):
        """ Set everything up"""
        self.session = get_session(config)
        with self.session_scope() as session:
            setup_db(session, config, confdir)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def log(self, source, target, flags, msg, type):
        """ Logs a message to the database

        | source: The source of the message.
        | target: The target of the message.
        | flags: Is the user a operator or voiced?
        | msg: The text of the message.
        | msg: The type of message.
        | time: The current time (Unix Epoch).
        """
        entry = Log(source=str(source), target=target, flags=flags, msg=msg, type=type, time=time())
        with self.session_scope() as session:
            session.add(entry)
            session.flush()
