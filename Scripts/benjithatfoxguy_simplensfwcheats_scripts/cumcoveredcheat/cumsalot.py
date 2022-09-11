from sims4.commands import Command, CommandType, CheatOutput, Output
import sims4.commands

@sims4.commands.Command('cumsalot', command_type=sims4.commands.CommandType.Live)
def cumsalotaction(_connection=None):
    sims4.commands.execute('ww.apply_cum face', None)
    sims4.commands.execute('ww.apply_cum chest', None)
    sims4.commands.execute('ww.apply_cum belly', None)
    sims4.commands.execute('ww.apply_cum back', None)
    sims4.commands.execute('ww.apply_cum lower_back', None)
    sims4.commands.execute('ww.apply_cum vagina', None)
    sims4.commands.execute('ww.apply_cum butt', None)
    sims4.commands.execute('ww.apply_cum feet', None)
    output = sims4.commands.CheatOutput(_connection)
    output('Sir cumsalot has arrived')