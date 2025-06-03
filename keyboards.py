import callbacks
import options

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

# ---- Keyboards ----

def initial_keyboard():
    scenario_callback_ids = options.initial_keyboard
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(scenario_id, callback_data=cb_id)]
        for scenario_id, cb_id in zip(options.initial_keyboard, scenario_callback_ids)
    ])
    
# TODO: Return to initial keyboard function
def return_to_initial_keyboard():
    pass

def scenario_selector_keyboard(scenario_keyboard):
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
        [InlineKeyboardButton(scenario, callback_data=scenario)]
        for scenario in scenario_keyboard
    ])

# Violence category keyboards

def pv_keyboard():
    return scenario_selector_keyboard(options.pv_keyboard)

def sh_keyboard():
    return scenario_selector_keyboard(options.sh_keyboard)

def dv_keyboard():
    return scenario_selector_keyboard(options.dv_keyboard)

def sa_keyboard():
    return scenario_selector_keyboard(options.sa_keyboard)   
 
def sr_keyboard():  
    return scenario_selector_keyboard(options.sr_keyboard)
    

# Intervention keyboards
# TODO: back function for every keyboard

def generic_branching_keyboard(keyboard_type):
    return lambda callbacks: \
        InlineKeyboardMarkup([
        [InlineKeyboardButton(option, callback_data=callback)]
        for option, callback in zip(keyboard_type, callbacks)
    ])

def intervention_keyboard(callbacks):
    return generic_branching_keyboard(options.intervention_keyboard)(callbacks)
    
def five_point_formula_keyboard(callbacks):
    return generic_branching_keyboard(options.five_point_formula_keyboard)(callbacks)

def five_cq_keyboard(callbacks):
    return generic_branching_keyboard(options.five_cq_keyboard)(callbacks)

def pv_s1_keyboard():
    return intervention_keyboard(callbacks.pv1_callbacks)

def pv_s2_keyboard():
    return intervention_keyboard(callbacks.pv2_callbacks)

def sh_s1_keyboard():
    return intervention_keyboard(callbacks.sh1_callbacks)

def sh_s2_keyboard():
    return intervention_keyboard(callbacks.sh2_callbacks)

def dv_s1_keyboard():
    return five_cq_keyboard(callbacks.dv1_callbacks)

def dv_s2_keyboard():
    return intervention_keyboard(callbacks.dv2_callbacks)

def sa_s1_keyboard():
    return five_cq_keyboard(callbacks.sa1_callbacks)

def sa_s2_keyboard():
    return five_point_formula_keyboard(callbacks.sa2_callbacks)

def sr_s1_keyboard():
    return five_point_formula_keyboard(callbacks.sr1_callbacks)

def sr_s2_keyboard():
    return five_cq_keyboard(callbacks.sr2_callbacks)
