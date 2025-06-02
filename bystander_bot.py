import branching
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
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    print(f"Received callback query: {query.data} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await query.answer()

    if query.data in options.initial_keyboard:
        print(f"Branching for violence type: {query.data}")
        await branching.violence_type_branching(query)

    elif query.data in options.pv_keyboard:
        print(f"Branching for peer violence scenario: {query.data}")
        await branching.pv_scenario_branching(query)

    elif query.data in options.sh_keyboard:
        print(f"Branching for sexual harassment scenario: {query.data}")
        await branching.sh_scenario_branching(query)

    elif query.data in options.dv_keyboard:
        print(f"Branching for domestic violence scenario: {query.data}")
        await branching.dv_scenario_branching(query)
        
    elif query.data in options.sa_keyboard:
        print(f"Branching for substance abuse scenario: {query.data}")
        await branching.sa_scenario_branching(query)
        
    elif query.data in options.sr_keyboard:
        print(f"Branching for suicide risk scenario: {query.data}")
        await branching.sr_scenario_branching(query)
        
    # TODO: Branching into intervention/5-point formula/5 core question explanations

# --- Main ---

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
