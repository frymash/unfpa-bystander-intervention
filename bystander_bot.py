import branching
import callbacks
import keyboards
import messages
import options
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# ---- Handlers ----

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(messages.welcome, reply_markup=keyboards.initial_keyboard())


# TODO: Implement the scenario selection logic
# TODO: Condense scenario selection logic into a single function
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    print(f"Received callback query: {query.data} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await query.answer()
    
    if query.data == callbacks.start:
        await query.edit_message_text(messages.welcome, reply_markup=keyboards.initial_keyboard())

    elif query.data in options.initial_keyboard:
        print(f"Branching for violence type: {query.data}")
        await branching.violence_type_branching(query)

    elif query.data in options.scenario_list:
        print(f"Branching for scenario: {query.data}")
        # Handle branching into specific scenarios
        await branching.handle_scenario_branching(query)
        
    # TODO: Branching into intervention/5-point formula/5 core question explanations
    elif query.data in callbacks.scenario_actions:
        print(f"Branching for intervention: {query.data}")
        # Handle branching into interventions
        await branching.handle_intervention_branching(query)


# --- Main ---

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
