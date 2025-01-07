from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes
import random
import json

TOKEN = '7719463736:AAEvUBNCGfvR-TXCPYuFWT4_Z7UpjYuiyCs'

# Load vocabulary data
with open("vocabulary.json", "r", encoding="utf-8") as file:
    vocabulary = json.load(file)

# Command: Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! I'm a German A1 Library.\n"
        "Made especially to practice German A1\n"
        "To get started, Hit /help"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "You can use the following commands:\n"
        "/define <word> - Get the definition and examples of a word.\n"
        "/random - Get a random word with its details.\n"
        "/search <word> - Search for the German equivalent of an English word.\n"
        "/say <word> - Get a voice of the pronunciation (not implemented yet)."
    )


# Command: Random
async def random_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    word = random.choice(vocabulary)
    await update.message.reply_text(
        f"- {word['German']}:\n"
        f"    {word['Translation']}\n\n"
        f"Example:\n{word['Example']}\n"
        f"{word['ExampleTranslation']}"
    )


# Command: Define
async def define(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide English word or phrase. Usage: /search <word>")
        return

    search_term = " ".join(context.args).lower()
    results = [
        word for word in vocabulary if search_term in word["German"].lower()
    ]

    if results:
        response = "Results:\n"
        for word in results[:5]:  # Limit to 5 results
            response += (
                f"- {word['German']}\n"
                f"     {word['Translation']}\n"
                f"   {word['Example']}\n"
                f"      {word['ExampleTranslation']}\n\n"
            )
        await update.message.reply_text(response)
    else:
        await update.message.reply_text(f"No results found for '{search_term}'.")


# Command: Search
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide an English word or phrase. Usage: /search <word>")
        return

    search_term = " ".join(context.args).lower()
    results = [
        word for word in vocabulary if search_term in word["Translation"].lower()
    ]

    if results:
        response = "Search Results:\n"
        for word in results[:5]:  # Limit to 5 results
            response += (
                f"- {word['German']}\n"
                f"    {word['Translation']}\n\n"
            )
        await update.message.reply_text(response)
    else:
        await update.message.reply_text(f"No results found for '{search_term}'.")


# Main function to run the bot
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("random", random_word))
    application.add_handler(CommandHandler("define", define))
    application.add_handler(CommandHandler("search", search))

    # Run the bot
    application.run_polling()


if __name__ == "__main__":
    main()
