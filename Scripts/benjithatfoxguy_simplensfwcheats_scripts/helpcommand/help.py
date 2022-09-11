from sims4.commands import Command, CommandType, CheatOutput
@Command('simplensfwcheatshelp', command_type=CommandType.Live)
def helpCommand(_connection=None):
    output = CheatOutput(_connection)
    output('Help for the Simple NSFW Cheats Mod')
    output('By BenjiThatFoxGuy')
    output('Currently available cheats:')
    output('cover the whole sim in cum - cumsalot')
    output('clear cum from sim - removecum, uncum')
    output('clear cum from all sims - removecumall, uncumall')
    output('get hard for 900 seconds - viagra, boner')
    output('stop having a boner - softy, bonerkill')