const API_BASE_URL = 'http://localhost:5000/api';

export const api = {
  // Check server status
  getStatus: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/status`);
      return await response.json();
    } catch (error) {
      console.error('Server connection failed:', error);
      return { server: 'offline', error: error.message };
    }
  },

  // Launch Person Re-ID
  launchReID: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/launch/reid`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      return await response.json();
    } catch (error) {
      return { success: false, message: 'Failed to connect to server' };
    }
  },

  // Launch Harry Potter Cloak
  launchCloak: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/launch/cloak`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      return await response.json();
    } catch (error) {
      return { success: false, message: 'Failed to connect to server' };
    }
  },

  // Stop a specific project
  stopProject: async (project) => {
    try {
      const response = await fetch(`${API_BASE_URL}/stop/${project}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      return await response.json();
    } catch (error) {
      return { success: false, message: 'Failed to connect to server' };
    }
  },

  // Stop all projects
  stopAll: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/stop/all`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      return await response.json();
    } catch (error) {
      return { success: false, message: 'Failed to connect to server' };
    }
  }
};

export default api;
