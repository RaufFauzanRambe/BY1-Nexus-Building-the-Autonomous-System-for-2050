"""
BY1-Nexus Configuration Module
==============================

Central configuration management for the autonomous AI system.
Supports environment variables and YAML configuration files.

Author: BY1-Nexus Team
Version: 1.0.0
"""

import os
from pathlib import Path
from typing import Any, Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class ModelConfig(BaseModel):
    """Configuration for the ML model architecture and training parameters."""
    
    input_dim: int = Field(default=10, description="Input feature dimension")
    hidden_dims: list[int] = Field(
        default=[64, 32, 16], 
        description="Hidden layer dimensions"
    )
    output_dim: int = Field(default=1, description="Output dimension")
    dropout_rate: float = Field(default=0.2, description="Dropout probability")
    learning_rate: float = Field(default=0.001, description="Optimizer learning rate")
    batch_size: int = Field(default=32, description="Training batch size")
    epochs: int = Field(default=100, description="Number of training epochs")
    early_stopping_patience: int = Field(default=10, description="Early stopping patience")
    

class DataConfig(BaseModel):
    """Configuration for data processing and feature engineering."""
    
    raw_data_path: str = Field(
        default="data/raw/sensor_data.csv",
        description="Path to raw data file"
    )
    processed_data_path: str = Field(
        default="data/processed/processed_data.csv",
        description="Path to save processed data"
    )
    model_save_path: str = Field(
        default="data/processed/model.pt",
        description="Path to save trained model"
    )
    train_test_split: float = Field(default=0.8, description="Training data ratio")
    normalize: bool = Field(default=True, description="Whether to normalize features")
    feature_columns: list[str] = Field(
        default=[
            "temperature", "pressure", "humidity", "vibration",
            "power_consumption", "rpm", "load", "efficiency",
            "runtime_hours", "error_count"
        ],
        description="Feature column names"
    )
    

class APIConfig(BaseModel):
    """Configuration for the FastAPI application."""
    
    host: str = Field(default="0.0.0.0", description="API server host")
    port: int = Field(default=8000, description="API server port")
    debug: bool = Field(default=True, description="Debug mode toggle")
    cors_origins: list[str] = Field(
        default=["*"],
        description="Allowed CORS origins"
    )
    api_prefix: str = Field(default="/api/v1", description="API route prefix")


class AnomalyThresholds(BaseModel):
    """Thresholds for anomaly detection classification."""
    
    low_risk: float = Field(default=0.3, description="Low risk threshold")
    medium_risk: float = Field(default=0.6, description="Medium risk threshold")
    high_risk: float = Field(default=0.8, description="High risk threshold")


class Settings(BaseSettings):
    """
    Main application settings.
    
    Loads configuration from environment variables with fallback defaults.
    Provides centralized access to all configuration parameters.
    """
    
    # Application metadata
    app_name: str = "BY1-Nexus"
    app_version: str = "1.0.0"
    app_description: str = "Building the Autonomous System for 2050"
    environment: str = "development"
    
    # Nested configurations
    model: ModelConfig = Field(default_factory=ModelConfig)
    data: DataConfig = Field(default_factory=DataConfig)
    api: APIConfig = Field(default_factory=APIConfig)
    thresholds: AnomalyThresholds = Field(default_factory=AnomalyThresholds)
    
    # Paths
    base_dir: Path = Field(
        default_factory=lambda: Path(__file__).parent,
        description="Base directory for the application"
    )
    
    class Config:
        env_prefix = "BY1_"
        env_nested_delimiter = "__"
        

# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Dependency injection function for FastAPI.
    
    Returns:
        Settings: Application settings instance
    """
    return settings


def update_settings(**kwargs: Any) -> None:
    """
    Update settings dynamically at runtime.
    
    Args:
        **kwargs: Configuration key-value pairs to update
    """
    global settings
    for key, value in kwargs.items():
        if hasattr(settings, key):
            setattr(settings, key, value)
