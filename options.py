# Initial keyboard options
pv = 'Peer violence'
sh = 'Sexual harassment'
dv = 'Domestic violence'
sa = 'Substance abuse'
sr = 'Suicide risk'

initial_keyboard = [pv, sh, dv, sa, sr]

# Peer violence introduction options
pv_classroom = 'Classroom'
pv_field = 'Field'
pv_keyboard = [pv_classroom, pv_field]

# Sexual harassment introduction options
sh_tram = 'Tram'
sh_school = 'School'
sh_keyboard = [sh_tram, sh_school]

# Domestic violence introduction options
dv_apartment = 'Apartment'
dv_livingroom = 'Living Room'
dv_keyboard = [dv_apartment, dv_livingroom]

# Substance abuse introduction options
sa_party = 'Party'
sa_friends_home = "Friend's home"
sa_keyboard = [sa_party, sa_friends_home]

# Suicide risk introduction options
sr_cafeteria = 'Cafeteria'
sr_lockerroom = 'Locker room'
sr_keyboard = [sr_cafeteria, sr_lockerroom]

# Unified scenario list
scenario_list = pv_keyboard \
    + sh_keyboard \
    + dv_keyboard \
    + sa_keyboard \
    + sr_keyboard

# Bystander intervention options
intervention_distract = 'Distract'
intervention_delegate = 'Delegate'
intervention_document = 'Document'
intervention_delay = 'Delay'
intervention_direct = 'Direct'

intervention_keyboard = [
    intervention_distract,
    intervention_delegate,
    intervention_document,
    intervention_delay,
    intervention_direct
]

# 5-point formula
i_care = 'I Care'
i_see = 'I See'
i_feel = 'I Feel'
i_want = 'I Want'
i_will = 'I Will'

five_point_formula_keyboard = [
    i_care,
    i_see,
    i_feel,
    i_want,
    i_will
]

# 5 core questions
five_cq_keyboard = [
    'Find the goal',
    'Decide how to intervene',
    'Weigh my options',
    'Find the costs/rewards',
    "Take the victim's perspective"
]
