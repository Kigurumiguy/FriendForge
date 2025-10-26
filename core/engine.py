#!/usr/bin/env python3
"""
FriendForge Engine - Multi-Bot Chat System

Project: FriendForge - The Living Chatbot Ensemble
Author: Kigurumiguy
License: MIT License

Description:
    Core engine for managing multiple chatbots in a single environment.
    Handles message routing, bot lifecycle, and communication between
    bots and users. Each bot has unique personality, voice, and functions.
    
    This engine supports both local (offline) and API-connected modes,
    allowing flexible deployment options.
"""

import json
import os
from typing import List, Dict, Optional, Any
from pathlib import Path


class Bot:
    """
    Base class for individual chatbot characters.
    
    Each bot has a unique personality defined by configuration and
    can respond to messages from users or other bots.
    """
    
    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize a bot with name and configuration.
        
        Args:
            name: Unique identifier for the bot
            config: Dictionary containing personality traits, voice style, etc.
        """
        self.name = name
        self.config = config
        self.personality = config.get('personality', {})
        self.voice_style = config.get('voice_style', 'neutral')
        self.quirks = config.get('quirks', [])
        self.history = []  # Conversation history for this bot
    
    def process_message(self, message: str, sender: str) -> str:
        """
        Process incoming message and generate response.
        
        Args:
            message: The message content
            sender: Who sent the message (user or another bot)
            
        Returns:
            Bot's response as a string
        """
        # TODO: Implement actual response generation
        # This is a stub that will be expanded with AI logic
        self.history.append({'sender': sender, 'message': message})
        return f"[{self.name}] Received message from {sender}: {message}"
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get bot information and current state.
        
        Returns:
            Dictionary with bot details
        """
        return {
            'name': self.name,
            'personality': self.personality,
            'voice_style': self.voice_style,
            'quirks': self.quirks,
            'message_count': len(self.history)
        }


class MessageRouter:
    """
    Routes messages between bots and users.
    
    Manages the conversation flow, determines which bot(s) should respond,
    and handles group chat dynamics when multiple bots interact.
    """
    
    def __init__(self, mode: str = 'local'):
        """
        Initialize the message router.
        
        Args:
            mode: Operating mode - 'local' for offline, 'api' for connected
        """
        self.bots: Dict[str, Bot] = {}
        self.mode = mode
        self.conversation_history = []
        self.host_bot = None  # Special bot that moderates
    
    def register_bot(self, bot: Bot):
        """
        Register a bot with the router.
        
        Args:
            bot: Bot instance to register
        """
        self.bots[bot.name] = bot
        if 'host' in bot.name.lower() or bot.config.get('role') == 'host':
            self.host_bot = bot
    
    def route_message(self, message: str, sender: str = 'user', 
                     target: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Route a message to appropriate bot(s) and collect responses.
        
        Args:
            message: Message content
            sender: Who sent the message
            target: Specific bot to target (None = all bots can respond)
            
        Returns:
            List of response dictionaries with 'bot' and 'response' keys
        """
        self.conversation_history.append({
            'sender': sender,
            'message': message,
            'target': target
        })
        
        responses = []
        
        # If target specified, route to that bot only
        if target and target in self.bots:
            response = self.bots[target].process_message(message, sender)
            responses.append({'bot': target, 'response': response})
        else:
            # TODO: Implement smart routing logic
            # For now, let host bot respond or first bot if no host
            responding_bot = self.host_bot if self.host_bot else list(self.bots.values())[0]
            if responding_bot:
                response = responding_bot.process_message(message, sender)
                responses.append({'bot': responding_bot.name, 'response': response})
        
        return responses
    
    def enable_group_chat_mode(self):
        """
        Enable group chat mode where multiple bots can respond and interact.
        
        TODO: Implement logic for bots to riff off each other
        """
        # Stub for future implementation
        pass
    
    def get_active_bots(self) -> List[str]:
        """
        Get list of currently active bot names.
        
        Returns:
            List of bot names
        """
        return list(self.bots.keys())


def load_characters_from_folder(folder_path: str = './characters') -> List[Dict[str, Any]]:
    """
    Load all character configuration files from the characters folder.
    
    Args:
        folder_path: Path to the characters directory
        
    Returns:
        List of character configuration dictionaries
    """
    characters = []
    char_folder = Path(folder_path)
    
    if not char_folder.exists():
        print(f"Warning: Characters folder '{folder_path}' not found")
        return characters
    
    # Load all JSON files from characters folder
    for file_path in char_folder.glob('*.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                character_data = json.load(f)
                characters.append(character_data)
                print(f"Loaded character: {character_data.get('name', 'Unknown')}")
        except json.JSONDecodeError as e:
            print(f"Error loading {file_path}: {e}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return characters


def initialize_local_mode(router: MessageRouter, characters: List[Dict[str, Any]]):
    """
    Initialize engine in local (offline) mode.
    
    Args:
        router: MessageRouter instance
        characters: List of character configurations
    """
    print("Initializing FriendForge in LOCAL mode (offline)...")
    
    # Create and register bots from character configs
    for char_config in characters:
        bot = Bot(char_config.get('name', 'Unknown'), char_config)
        router.register_bot(bot)
    
    print(f"Registered {len(router.get_active_bots())} bots: {', '.join(router.get_active_bots())}")
    # TODO: Initialize local language model or rule-based responses


def initialize_api_mode(router: MessageRouter, characters: List[Dict[str, Any]], 
                       api_config: Optional[Dict[str, str]] = None):
    """
    Initialize engine in API mode (connects to external AI models).
    
    Args:
        router: MessageRouter instance
        characters: List of character configurations
        api_config: API configuration (endpoints, keys, etc.)
    """
    print("Initializing FriendForge in API mode (connected)...")
    
    # Create and register bots from character configs
    for char_config in characters:
        bot = Bot(char_config.get('name', 'Unknown'), char_config)
        router.register_bot(bot)
    
    print(f"Registered {len(router.get_active_bots())} bots: {', '.join(router.get_active_bots())}")
    # TODO: Initialize API connections to external AI services
    # TODO: Validate API credentials and endpoints


def main():
    """
    Main entry point for FriendForge engine.
    
    Loads characters, initializes the message router, and starts the chat system.
    """
    print("="*50)
    print("FriendForge - The Living Chatbot Ensemble")
    print("="*50)
    
    # Load character configurations
    characters = load_characters_from_folder('./characters')
    
    if not characters:
        print("No characters found. Please add character JSON files to ./characters folder.")
        return
    
    # Initialize message router
    # TODO: Add command-line arguments to choose mode
    mode = 'local'  # Default to local mode
    router = MessageRouter(mode=mode)
    
    # Initialize based on selected mode
    if mode == 'local':
        initialize_local_mode(router, characters)
    elif mode == 'api':
        initialize_api_mode(router, characters)
    else:
        print(f"Unknown mode: {mode}")
        return
    
    print("\nFriendForge engine initialized successfully!")
    print(f"Active bots: {len(router.get_active_bots())}")
    print("\nReady for interaction...\n")
    
    # TODO: Start interactive chat loop or connect to interface
    # For now, just demonstrate basic functionality
    test_message = "Hello everyone!"
    print(f"User: {test_message}")
    responses = router.route_message(test_message, sender='user')
    for resp in responses:
        print(f"{resp['bot']}: {resp['response']}")


if __name__ == '__main__':
    main()
