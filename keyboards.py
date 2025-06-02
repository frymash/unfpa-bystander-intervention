import options

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

# ---- Keyboards ----

def initial_keyboard():
    scenario_callback_ids = options.initial_keyboard
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(scenario_id, callback_data=cb_id)]
        for scenario_id, cb_id in zip(options.initial_keyboard, scenario_callback_ids)
    ])

def selector_keyboard(next_keyboard):
    """A generic keyboard that allows users to access different interventions or scenarios relevant to a given
    category of violence.

    Args:
        scenario_keyboard (list(str)): a keyboard with scenarios relevant to a given category of violence.
        
        e.g. this could be a keyboard linked to scenarios relevant to peer violence.
        Such a keyboard could look like this: ['Classroom', 'Field'].
        This keyboard would branch out to two peer violence scenarios located in the 'Classroom' and 'Field'.

    Returns:
        InlineKeyboardMarkup: keyboard with follow-up options
    """
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(option, callback_data=option)]
        for option in next_keyboard
    ])

# Violence category keyboards

def pv_keyboard():
    return selector_keyboard(options.pv_keyboard)

def sh_keyboard():
    return selector_keyboard(options.sh_keyboard)

def dv_keyboard():
    return selector_keyboard(options.dv_keyboard)

def sa_keyboard():
    return selector_keyboard(options.sa_keyboard)   
 
def sr_keyboard():  
    return selector_keyboard(options.sr_keyboard)
    

# Intervention keyboards
# TODO: create new keyboard for each intervention type in each scenarios
# TODO: back function for every keyboard
# currently, all intervention keyboards produce the same callback data
# 1 keyboard for each scenario??

def intervention_keyboard():
    return selector_keyboard(options.intervention_keyboard)

def five_point_formula_keyboard():
    return selector_keyboard(options.five_point_formula_keyboard)

def five_cq_keyboard():
    return selector_keyboard(options.five_cq_keyboard)
