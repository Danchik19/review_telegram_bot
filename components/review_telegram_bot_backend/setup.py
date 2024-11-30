from setuptools import setup, find_packages


with open("./review_telegram_bot/reqiurements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="review_telegram_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "review_telegram_bot=review_telegram_bot.composites.runner:main",
        ],
    },
    author="Hedgehogs Digital",
    description="Telegram bot for code review",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Danchik19/review_telegram_bot.git",
    python_requires=">=3.11.5",
)
