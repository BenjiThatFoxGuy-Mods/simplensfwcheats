from sims4.commands import Command, CommandType, CheatOutput, Output

import sims4.commands

@sims4.commands.Command('softy', command_type=sims4.commands.CommandType.Live)
def bonerkillaction(_connection=None):
    sims4.commands.execute('ww.get_soft', None)
    output = sims4.commands.CheatOutput(_connection)
    output('boner removal')

@sims4.commands.Command('bonerkill', command_type=sims4.commands.CommandType.Live)
def bonerkillactionalias(_connection=None):
    sims4.commands.execute('softy', None)
    output = sims4.commands.CheatOutput(_connection)