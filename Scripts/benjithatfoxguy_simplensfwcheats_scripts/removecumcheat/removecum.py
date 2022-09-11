from sims4.commands import Command, CommandType, CheatOutput, Output
import sims4.commands


@sims4.commands.Command('removecum', command_type=sims4.commands.CommandType.Live)
def cumsalotaction(_connection=None):
    sims4.commands.execute('ww.clear_cum', None)
    output = sims4.commands.CheatOutput(_connection)
    output(':(')


@sims4.commands.Command('uncum', command_type=sims4.commands.CommandType.Live)
def cumsalotaction(_connection=None):
    sims4.commands.execute('removecum', None)
    output = sims4.commands.CheatOutput(_connection)


@sims4.commands.Command('removecumall', command_type=sims4.commands.CommandType.Live)
def uncumeveryoneaction(_connection=None):
    sims4.commands.execute('ww.clear_all_cum', None)
    output = sims4.commands.CheatOutput(_connection)
    output(':/')


@sims4.commands.Command('uncumall', command_type=sims4.commands.CommandType.Live)
def cumsalotaction(_connection=None):
    sims4.commands.execute('removecumall', None)
    output = sims4.commands.CheatOutput(_connection)
