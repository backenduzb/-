from aiogram import Router, types, Bot, F
from aiogram.filters import Command
from aiogram.utils.chat_action import ChatActionSender
from aiogram.enums import ChatAction
from .writer import write
from config.settings import ADMIN_ID
import asyncio
