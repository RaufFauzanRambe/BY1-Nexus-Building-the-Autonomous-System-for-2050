/**
 * BY1-Nexus API Mini Service Entry Point
 * 
 * This file serves as the entry point for the BY1-Nexus AI backend service.
 * The actual API server is started via the package.json scripts using uvicorn.
 * 
 * The service runs on port 3031 and provides:
 * - /api/v1/predict - Anomaly prediction endpoints
 * - /api/v1/train - Model training endpoints
 * - /api/v1/system - System health and info
 * - /api/v1/data - Data management endpoints
 */

// Service metadata
export const SERVICE_NAME = 'BY1-Nexus API';
export const SERVICE_VERSION = '1.0.0';
export const SERVICE_PORT = 3031;
export const SERVICE_DESCRIPTION = 'Autonomous AI System for Anomaly Detection';

// The actual Python FastAPI server is started via:
// uvicorn api.main:app --host 0.0.0.0 --port 3031 --reload
