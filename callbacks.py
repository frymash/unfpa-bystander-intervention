start = 'start'

# 1.1 Scenario 1: Older student bullies younger student in elementary school
pv1_distract = 'pv1_distract'
pv1_delegate = 'pv1_delegate'
pv1_document = 'pv1_document'
pv1_delay = 'pv1_delay'
pv1_direct = 'pv1_direct'
pv1_callbacks = [
    pv1_distract, pv1_delegate, pv1_document, pv1_delay, pv1_direct
]

# 1.2 Scenario 2: Racism against a Roma student in sports class
pv2_distract = 'pv2_distract'
pv2_delegate = 'pv2_delegate'
pv2_document = 'pv2_document'
pv2_delay = 'pv2_delay'
pv2_direct = 'pv2_direct'
pv2_callbacks = [
    pv2_distract, pv2_delegate, pv2_document, pv2_delay, pv2_direct
]

# 2.1 Scenario 1: Molestation on a tram
sh1_distract = 'sh1_distract'
sh1_delegate = 'sh1_delegate'
sh1_document = 'sh1_document'
sh1_delay = 'sh1_delay'
sh1_direct = 'sh1_direct'
sh1_callbacks = [
    sh1_distract, sh1_delegate, sh1_document, sh1_delay, sh1_direct
]

# 2.2 Scenario 2: Unsolicited explicit messages at school
sh2_distract = 'sh1_distract'
sh2_delegate = 'sh1_delegate'
sh2_document = 'sh1_document'
sh2_delay = 'sh1_delay'
sh2_direct = 'sh1_direct'
sh2_callbacks = [
    sh2_distract, sh2_delegate, sh2_document, sh2_delay, sh2_direct
]

# 3.1 Scenario 1: Child abuse in an apartment
dv1_goal = 'dv1_goal'
dv1_decision_making = 'dv1_decision_making'
dv1_intervention = 'dv1_intervention'
dv1_options = 'dv1_options'
dv1_cost_benefits = 'dv1_cost_benefits'
dv1_perspective_taking = 'dv1_perspective_taking'
dv1_callbacks = [
    dv1_goal, dv1_decision_making, dv1_intervention, 
    dv1_options, dv1_cost_benefits, dv1_perspective_taking
]

# 3.2 Scenario 2: Physical confrontation between parents at home
dv2_distract = 'dv2_distract'
dv2_delegate = 'dv2_delegate'
dv2_document = 'dv2_document'
dv2_delay = 'dv2_delay'
dv2_direct = 'dv2_direct'
dv2_callbacks = [
    dv2_distract, dv2_delegate, dv2_document, dv2_delay, dv2_direct
]

# 4.1 Scenario 1: Underage drinking at a party
sa1_goal = 'sa1_goal'
sa1_decision_making = 'sa1_decision_making'
sa1_intervention = 'sa1_intervention'
sa1_options = 'sa1_options'
sa1_cost_benefits = 'sa1_cost_benefits'
sa1_perspective_taking = 'sa1_perspective_taking'
sa1_callbacks = [
    sa1_goal, sa1_decision_making, sa1_intervention, 
    sa1_options, sa1_cost_benefits, sa1_perspective_taking
]


# 4.2 Scenario 2: Drug addiction at school
sa2_care = 'sa2_care'
sa2_see = 'sa2_see'
sa2_feel = 'sa2_feel'
sa2_want = 'sa2_want'
sa2_will = 'sa2_will'
sa2_callbacks = [
    sa2_care, sa2_see, sa2_feel, sa2_want, sa2_will
]

# 5.1 Scenario 1: Cafeteria
sr1_care = 'sr1_care'
sr1_see = 'sr1_see'
sr1_feel = 'sr1_feel'
sr1_want = 'sr1_want'
sr1_will = 'sr1_will'
sr1_callbacks = [
    sr1_care, sr1_see, sr1_feel, sr1_want, sr1_will
]

# 5.2 Scenario 2: Locker room
sr2_goal = 'sr2_goal'
sr2_decision_making = 'sr2_decision_making'
sr2_intervention = 'sr2_intervention'
sr2_options = 'sr2_options'
sr2_cost_benefits = 'sr2_cost_benefits'
sr2_perspective_taking = 'sr2_perspective_taking'
sr2_callbacks = [
    sr2_goal, sr2_decision_making, sr2_intervention, 
    sr2_options, sr2_cost_benefits, sr2_perspective_taking
]

# All callbacks for branching scenarios
pv_callbacks = pv1_callbacks + pv2_callbacks
sh_callbacks = sh1_callbacks + sh2_callbacks
dv_callbacks = dv1_callbacks + dv2_callbacks
sa_callbacks = sa1_callbacks + sa2_callbacks
sr_callbacks = sr1_callbacks + sr2_callbacks
scenario_actions = pv_callbacks + sh_callbacks + dv_callbacks + sa_callbacks + sr_callbacks
