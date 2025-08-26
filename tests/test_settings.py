#!/usr/bin/env python3
"""Test script to verify the settings and classifier configuration."""

import os
import pytest
from ai_classifier_sample.config.settings import get_settings
from ai_classifier_sample.service.classifier import MessageClassifier


class TestSettings:
    """Test class for settings functionality."""
    
    def test_settings_singleton(self):
        """Test the settings singleton behavior."""
        settings1 = get_settings()
        settings2 = get_settings()
        
        assert settings1 is settings2, "Settings should be a singleton"
    
    def test_default_values(self):
        """Test that default values are set correctly."""
        settings = get_settings()
        
        assert settings.cloud_region == "us-east-1"
        assert settings.cloud_profile == "tr-dev-power-user"  # From .env file
        assert settings.max_tokens == 5000
        assert settings.provider == "anthropic"  # From .env file
        assert "arn:aws:bedrock" in settings.model_arn

    def test_environment_override(self):
        """Test environment variable override."""
        # Set environment variables
        os.environ["CLOUD_REGION"] = "us-east-2"
        os.environ["CLOUD_PROFILE"] = "test-profile"
        
        # Clear the cache to get fresh settings
        get_settings.cache_clear()
        
        settings = get_settings()
        assert settings.cloud_region == "us-east-2"
        assert settings.cloud_profile == "test-profile"
        
        # Clean up
        del os.environ["CLOUD_REGION"]
        del os.environ["CLOUD_PROFILE"]
        get_settings.cache_clear()


class TestClassifier:
    """Test class for classifier functionality."""
    
    def test_classifier_initialization(self):
        """Test that the classifier can be initialized with settings."""
        classifier = MessageClassifier()
        assert classifier is not None
        assert classifier.llm is not None
    
    def test_classifier_basic_functionality(self):
        """Test basic classification functionality."""
        classifier = MessageClassifier()
        
        # Test single-turn classification
        message = "I need help with my order"
        result = classifier.classify(message)
        assert isinstance(result, str)
        assert "message" in result
        assert "category" in result


# Legacy function for direct execution (maintains backward compatibility)
def test_settings():
    """Test the settings singleton behavior."""
    print("Testing settings...")
    
    # Test singleton behavior
    settings1 = get_settings()
    settings2 = get_settings()
    
    assert settings1 is settings2, "Settings should be a singleton"
    print("✓ Settings singleton working correctly")
    
    # Test default values
    print(f"Cloud Region: {settings1.cloud_region}")
    print(f"Cloud Profile: {settings1.cloud_profile}")
    print(f"Model ARN: {settings1.model_arn}")
    print(f"Max Tokens: {settings1.max_tokens}")
    print(f"Provider: {settings1.provider}")


def test_environment_override():
    """Test environment variable override."""
    print("\nTesting environment variable override...")
    
    # Set an environment variable
    os.environ["CLOUD_REGION"] = "us-east-2"
    os.environ["CLOUD_PROFILE"] = "test-profile"
    
    # Clear the cache to get fresh settings
    get_settings.cache_clear()
    
    settings = get_settings()
    assert settings.cloud_region == "us-east-2", f"Expected us-east-2, got {settings.cloud_region}"
    assert settings.cloud_profile == "test-profile", f"Expected test-profile, got {settings.cloud_profile}"
    
    print("✓ Environment variable override working correctly")
    
    # Clean up
    del os.environ["CLOUD_REGION"]
    del os.environ["CLOUD_PROFILE"]
    get_settings.cache_clear()


def test_classifier_initialization():
    """Test that the classifier can be initialized with settings."""
    print("\nTesting classifier initialization...")
    
    try:
        classifier = MessageClassifier()
        print("✓ MessageClassifier initialized successfully")
    except Exception as e:
        print(f"✗ Failed to initialize MessageClassifier: {e}")


if __name__ == "__main__":
    print("Running AI Classifier Settings Tests")
    print("=" * 50)
    
    # Test settings
    test_settings()
    
    # Test environment override
    test_environment_override()
    
    # Test classifier
    test_classifier_initialization()
    
    print("\n" + "=" * 50)
    print("All tests completed!")