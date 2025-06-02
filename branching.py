import keyboards
import messages
import options

async def violence_type_branching(query):
    if query.data == options.pv:
        print(f"Activated peer violence scenario keyboard.")
        await query.edit_message_text(messages.pv_intro, reply_markup=keyboards.pv_keyboard())
    elif query.data == options.sh:
        print(f"Activated sexual harassment scenario keyboard.")
        await query.edit_message_text(messages.sh_intro, reply_markup=keyboards.sh_keyboard())
    elif query.data == options.dv:
        print(f"Activated domestic violence scenario keyboard.")
        await query.edit_message_text(messages.dv_intro, reply_markup=keyboards.dv_keyboard())
    elif query.data == options.sa:
        print(f"Activated substance abuse scenario keyboard.")
        await query.edit_message_text(messages.sa_intro, reply_markup=keyboards.sa_keyboard())
    elif query.data == options.sr:
        print(f"Activated suicide risk scenario keyboard.")
        await query.edit_message_text(messages.sr_intro, reply_markup=keyboards.sr_keyboard())
        
async def pv_scenario_branching(query):
    # 1.1 Scenario 1: Older student bullies younger student in elementary school
    if query.data == 'Classroom':
        await query.edit_message_text(messages.pv_scenario_1, reply_markup=keyboards.intervention_keyboard())
    # 1.2 Scenario 2: Racism against a Roma girl in sports class
    elif query.data == 'Field':
        await query.edit_message_text(messages.pv_scenario_2, reply_markup=keyboards.intervention_keyboard())
        

async def sh_scenario_branching(query):
    # 2.1 Scenario 1: Molestation on a tram
    if query.data == 'Tram':
        await query.edit_message_text(messages.sh_scenario_1, reply_markup=keyboards.intervention_keyboard())
    # 2.2 Scenario 2: Unsolicited explicit messages at school
    elif query.data == 'School':
        await query.edit_message_text(messages.sh_scenario_2, reply_markup=keyboards.intervention_keyboard())
        
async def dv_scenario_branching(query):
    # 3.1 Scenario 1: Child abuse in an apartment
    if query.data == 'Apartment':
        await query.edit_message_text(messages.dv_scenario_1, reply_markup=keyboards.five_cq_keyboard())
    # 3.2 Scenario 2: Physical confrontation between parents at home
    elif query.data == 'Living Room':
        await query.edit_message_text(messages.dv_scenario_2, reply_markup=keyboards.intervention_keyboard())
        
async def sa_scenario_branching(query):
    # 4.1 Scenario 1: Underage drinking at a party
    if query.data == 'Party':
        await query.edit_message_text(messages.sa_scenario_1, reply_markup=keyboards.five_cq_keyboard())
    # 4.2 Scenario 2: Drug addiction at school
    elif query.data == 'School':
        await query.edit_message_text(
            messages.sa_scenario_2, reply_markup=keyboards.five_point_formula_keyboard()
        )
        
async def sr_scenario_branching(query):
    if query.data == 'Lunchroom':
        await query.edit_message_text(messages.sr_scenario_1, reply_markup=keyboards.five_point_formula_keyboard())
    elif query.data == 'Bedroom':
        await query.edit_message_text(messages.sr_scenario_2, reply_markup=keyboards.five_cq_keyboard())
