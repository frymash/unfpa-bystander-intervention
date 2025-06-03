import callbacks
import keyboards
import messages
import options


async def violence_type_branching(query):
    if query.data == options.pv:
        print("Activated peer violence scenario keyboard.")
        await query.edit_message_text(messages.pv_intro, reply_markup=keyboards.pv_keyboard())
    elif query.data == options.sh:
        print("Activated sexual harassment scenario keyboard.")
        await query.edit_message_text(messages.sh_intro, reply_markup=keyboards.sh_keyboard())
    elif query.data == options.dv:
        print("Activated domestic violence scenario keyboard.")
        await query.edit_message_text(messages.dv_intro, reply_markup=keyboards.dv_keyboard())
    elif query.data == options.sa:
        print("Activated substance abuse scenario keyboard.")
        await query.edit_message_text(messages.sa_intro, reply_markup=keyboards.sa_keyboard())
    elif query.data == options.sr:
        print("Activated suicide risk scenario keyboard.")
        await query.edit_message_text(messages.sr_intro, reply_markup=keyboards.sr_keyboard())


async def handle_scenario_branching(query):
    if query.data in options.pv_keyboard:
        print(f"Branching for peer violence scenario: {query.data}")
        await pv_scenario_branching(query)

    elif query.data in options.sh_keyboard:
        print(f"Branching for sexual harassment scenario: {query.data}")
        await sh_scenario_branching(query)

    elif query.data in options.dv_keyboard:
        print(f"Branching for domestic violence scenario: {query.data}")
        await dv_scenario_branching(query)
        
    elif query.data in options.sa_keyboard:
        print(f"Branching for substance abuse scenario: {query.data}")
        await sa_scenario_branching(query)
        
    elif query.data in options.sr_keyboard:
        print(f"Branching for suicide risk scenario: {query.data}")
        await sr_scenario_branching(query)
        

# TODO: replace "if query.data == (string)" strings with variables from callbacks.py
async def pv_scenario_branching(query):
    # 1.1 Scenario 1: Older student bullies younger student in elementary school
    if query.data == 'Classroom':
        print("Branching into peer violence scenario 1")
        await query.edit_message_text(messages.pv_scenario_1, reply_markup=keyboards.pv_s1_keyboard())
    # 1.2 Scenario 2: Racism against a Roma girl in sports class
    elif query.data == 'Field':
        print("Branching into peer violence scenario 2")
        await query.edit_message_text(messages.pv_scenario_2, reply_markup=keyboards.pv_s2_keyboard())
        

async def sh_scenario_branching(query):
    # 2.1 Scenario 1: Molestation on a tram
    if query.data == 'Tram':
        print("Branching into sexual harassment scenario 1")
        await query.edit_message_text(messages.sh_scenario_1, reply_markup=keyboards.sh_s1_keyboard())
    # 2.2 Scenario 2: Unsolicited explicit messages at school
    elif query.data == 'School':
        await query.edit_message_text(messages.sh_scenario_2, reply_markup=keyboards.sh_s2_keyboard())


async def dv_scenario_branching(query):
    # 3.1 Scenario 1: Child abuse in an apartment
    if query.data == 'Apartment':
        await query.edit_message_text(messages.dv_scenario_1, reply_markup=keyboards.dv_s1_keyboard())
    # 3.2 Scenario 2: Physical confrontation between parents at home
    elif query.data == 'Living Room':
        await query.edit_message_text(messages.dv_scenario_2, reply_markup=keyboards.dv_s2_keyboard())

      
async def sa_scenario_branching(query):
    # 4.1 Scenario 1: Underage drinking at a party
    if query.data == 'Party':
        await query.edit_message_text(messages.sa_scenario_1, reply_markup=keyboards.sa_s1_keyboard())
    # 4.2 Scenario 2: Drug addiction at school
    elif query.data == 'School':
        await query.edit_message_text(messages.sa_scenario_2, reply_markup=keyboards.sa_s2_keyboard())

     
async def sr_scenario_branching(query):
    # 5.1 Scenario 1: 
    if query.data == 'Lunchroom':
        await query.edit_message_text(messages.sr_scenario_1, reply_markup=keyboards.sr_s1_keyboard())
    elif query.data == 'Locker room':
        await query.edit_message_text(messages.sr_scenario_2, reply_markup=keyboards.sr_s2_keyboard())
        
async def handle_intervention_branching(query):
    if query.data in callbacks.pv_callbacks:
        await handle_pv_intervention(query)
    elif query.data in callbacks.sh_callbacks:
        await handle_sh_intervention(query)
    elif query.data in callbacks.dv_callbacks:
        await handle_dv_intervention(query)
    elif query.data in callbacks.sa_callbacks:
        await handle_sa_intervention(query)
    elif query.data in callbacks.sr_callbacks:
        await handle_sr_intervention(query)
        
async def handle_pv_intervention(query):
    if query.data in callbacks.pv1_callbacks:
        await pv1_intervention_branching(query)
    elif query.data in callbacks.pv2_callbacks:
        await pv2_intervention_branching(query)

async def handle_sh_intervention(query):
    if query.data in callbacks.sh1_callbacks:
        await sh1_intervention_branching(query)
    elif query.data in callbacks.sh2_callbacks:
        await sh2_intervention_branching(query)

async def handle_dv_intervention(query):
    if query.data in callbacks.dv1_callbacks:
        await dv1_intervention_branching(query)
    elif query.data in callbacks.dv2_callbacks:
        await dv2_intervention_branching(query)

async def handle_sa_intervention(query):
    if query.data in callbacks.sa1_callbacks:
        await sa1_intervention_branching(query)
    elif query.data in callbacks.sa2_callbacks:
        await sa2_intervention_branching(query)

async def handle_sr_intervention(query):
    if query.data in callbacks.sr1_callbacks:
        await sr1_intervention_branching(query)
    elif query.data in callbacks.sr2_callbacks:
        await sr2_intervention_branching(query)
        
async def pv1_intervention_branching(query):
    if query.data == callbacks.pv1_distract:
        await query.edit_message_text(messages.pv1_distract)
    elif query.data == callbacks.pv1_delegate:
        await query.edit_message_text(messages.pv1_delegate)
    elif query.data == callbacks.pv1_document:
        await query.edit_message_text(messages.pv1_document)
    elif query.data == callbacks.pv1_delay:
        await query.edit_message_text(messages.pv1_delay)
    elif query.data == callbacks.pv1_direct:
        await query.edit_message_text(messages.pv1_direct)
        
async def pv2_intervention_branching(query):
    if query.data == callbacks.pv2_distract:
        await query.edit_message_text(messages.pv2_distract)
    elif query.data == callbacks.pv2_delegate:
        await query.edit_message_text(messages.pv2_delegate)
    elif query.data == callbacks.pv2_document:
        await query.edit_message_text(messages.pv2_document)
    elif query.data == callbacks.pv2_delay:
        await query.edit_message_text(messages.pv2_delay)
    elif query.data == callbacks.pv2_direct:
        await query.edit_message_text(messages.pv2_direct)

async def sh1_intervention_branching(query):
    if query.data == callbacks.sh1_distract:
        await query.edit_message_text(messages.sh1_distract)
    elif query.data == callbacks.sh1_delegate:
        await query.edit_message_text(messages.sh1_delegate)
    elif query.data == callbacks.sh1_document:
        await query.edit_message_text(messages.sh1_document)
    elif query.data == callbacks.sh1_delay:
        await query.edit_message_text(messages.sh1_delay)
    elif query.data == callbacks.sh1_direct:
        await query.edit_message_text(messages.sh1_direct)

async def sh2_intervention_branching(query):
    if query.data == callbacks.sh2_distract:
        await query.edit_message_text(messages.sh2_distract)
    elif query.data == callbacks.sh2_delegate:
        await query.edit_message_text(messages.sh2_delegate)
    elif query.data == callbacks.sh2_document:
        await query.edit_message_text(messages.sh2_document)
    elif query.data == callbacks.sh2_delay:
        await query.edit_message_text(messages.sh2_delay)
    elif query.data == callbacks.sh2_direct:
        await query.edit_message_text(messages.sh2_direct)

async def dv1_intervention_branching(query):
    if query.data == callbacks.dv1_goal:
        await query.edit_message_text(messages.dv1_goal)
    elif query.data == callbacks.dv1_decision_making:
        await query.edit_message_text(messages.dv1_decision_making)
    elif query.data == callbacks.dv1_intervention:
        await query.edit_message_text(messages.dv1_intervention)
    elif query.data == callbacks.dv1_options:
        await query.edit_message_text(messages.dv1_options)
    elif query.data == callbacks.dv1_cost_benefits:
        await query.edit_message_text(messages.dv1_cost_benefits)
    elif query.data == callbacks.dv1_perspective_taking:
        await query.edit_message_text(messages.dv1_perspective_taking)

async def dv2_intervention_branching(query):
    if query.data == callbacks.dv2_distract:
        await query.edit_message_text(messages.dv2_distract)
    elif query.data == callbacks.dv2_delegate:
        await query.edit_message_text(messages.dv2_delegate)
    elif query.data == callbacks.dv2_document:
        await query.edit_message_text(messages.dv2_document)
    elif query.data == callbacks.dv2_delay:
        await query.edit_message_text(messages.dv2_delay)
    elif query.data == callbacks.dv2_direct:
        await query.edit_message_text(messages.dv2_direct)

async def sa1_intervention_branching(query):
    if query.data == callbacks.sa1_goal:
        await query.edit_message_text(messages.sa1_goal)
    elif query.data == callbacks.sa1_decision_making:
        await query.edit_message_text(messages.sa1_decision_making)
    elif query.data == callbacks.sa1_intervention:
        await query.edit_message_text(messages.sa1_intervention)
    elif query.data == callbacks.sa1_options:
        await query.edit_message_text(messages.sa1_options)
    elif query.data == callbacks.sa1_cost_benefits:
        await query.edit_message_text(messages.sa1_cost_benefits)
    elif query.data == callbacks.sa1_perspective_taking:
        await query.edit_message_text(messages.sa1_perspective_taking)

async def sa2_intervention_branching(query):
    if query.data == callbacks.sa2_distract:
        await query.edit_message_text(messages.sa2_distract)
    elif query.data == callbacks.sa2_delegate:
        await query.edit_message_text(messages.sa2_delegate)
    elif query.data == callbacks.sa2_document:
        await query.edit_message_text(messages.sa2_document)
    elif query.data == callbacks.sa2_delay:
        await query.edit_message_text(messages.sa2_delay)
    elif query.data == callbacks.sa2_direct:
        await query.edit_message_text(messages.sa2_direct)

async def sr1_intervention_branching(query):
    if query.data == callbacks.sr1_care:
        await query.edit_message_text(messages.sr1_care)
    elif query.data == callbacks.sr1_see:
        await query.edit_message_text(messages.sr1_see)
    elif query.data == callbacks.sr1_feel:
        await query.edit_message_text(messages.sr1_feel)
    elif query.data == callbacks.sr1_want:
        await query.edit_message_text(messages.sr1_want)
    elif query.data == callbacks.sr1_will:
        await query.edit_message_text(messages.sr1_will)

async def sr2_intervention_branching(query):
    if query.data == callbacks.sr2_goal:
        await query.edit_message_text(messages.sr2_goal)
    elif query.data == callbacks.sr2_decision_making:
        await query.edit_message_text(messages.sr2_decision_making)
    elif query.data == callbacks.sr2_intervention:
        await query.edit_message_text(messages.sr2_intervention)
    elif query.data == callbacks.sr2_options:
        await query.edit_message_text(messages.sr2_options)
    elif query.data == callbacks.sr2_cost_benefits:
        await query.edit_message_text(messages.sr2_cost_benefits)
    elif query.data == callbacks.sr2_perspective_taking:
        await query.edit_message_text(messages.sr2_perspective_taking)
        
