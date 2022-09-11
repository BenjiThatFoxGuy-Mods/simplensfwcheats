from sims4.commands import Command, CommandType, CheatOutput, Output

import sims4.commands

@sims4.commands.Command('viagra', command_type=sims4.commands.CommandType.Live)
def boneraction(_connection=None):
    sims4.commands.execute('ww.get_hard 900', None)
    output = sims4.commands.CheatOutput(_connection)
    output('You have becum hard')

@sims4.commands.Command('boner', command_type=sims4.commands.CommandType.Live)
def boneractionalias(_connection=None):
    sims4.commands.execute('viagra', None)
    output = sims4.commands.CheatOutput(_connection)