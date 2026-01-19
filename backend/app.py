"""
Flask Backend Server for Person Re-ID Project
Handles launching ML models and managing processes
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os
import sys
import signal
import psutil

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Store running processes
running_processes = {}

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Use py launcher on Windows (has ML dependencies installed)
if os.name == 'nt':
    # Try py -3 first (Windows Python launcher)
    PYTHON_PATH = 'py'
    PYTHON_ARGS = ['-3']
else:
    PYTHON_PATH = sys.executable
    PYTHON_ARGS = []

@app.route('/api/status', methods=['GET'])
def get_status():
    """Check server status and running processes"""
    status = {}
    for name, proc in list(running_processes.items()):
        if proc and proc.poll() is None:
            status[name] = 'running'
        else:
            status[name] = 'stopped'
            if name in running_processes:
                del running_processes[name]
    
    return jsonify({
        'server': 'online',
        'python_path': PYTHON_PATH,
        'project_root': PROJECT_ROOT,
        'processes': status
    })

@app.route('/api/launch/reid', methods=['POST'])
def launch_reid():
    """Launch Person Re-Identification model"""
    try:
        # Check if already running
        if 'reid' in running_processes and running_processes['reid'].poll() is None:
            return jsonify({
                'success': False,
                'message': 'Person Re-ID is already running',
                'status': 'running'
            })
        
        # Path to the re-id script
        reid_script = os.path.join(PROJECT_ROOT, 'reidentification', 'realtime_reid_robust.py')
        
        if not os.path.exists(reid_script):
            return jsonify({
                'success': False,
                'message': f'Script not found: {reid_script}'
            }), 404
        
        # Launch the process
        process = subprocess.Popen(
            [PYTHON_PATH] + PYTHON_ARGS + [reid_script],
            cwd=os.path.join(PROJECT_ROOT, 'reidentification'),
            creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0
        )
        
        running_processes['reid'] = process
        
        return jsonify({
            'success': True,
            'message': 'Person Re-ID launched successfully!',
            'pid': process.pid,
            'status': 'running'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/launch/cloak', methods=['POST'])
def launch_cloak():
    """Launch Harry Potter Invisible Cloak"""
    try:
        # Check if already running
        if 'cloak' in running_processes and running_processes['cloak'].poll() is None:
            return jsonify({
                'success': False,
                'message': 'Harry Potter Cloak is already running',
                'status': 'running'
            })
        
        # Path to the cloak script
        cloak_script = os.path.join(PROJECT_ROOT, 'harry-potter-cloak', 'harry.py')
        
        if not os.path.exists(cloak_script):
            return jsonify({
                'success': False,
                'message': f'Script not found: {cloak_script}'
            }), 404
        
        # Launch the process
        process = subprocess.Popen(
            [PYTHON_PATH] + PYTHON_ARGS + [cloak_script],
            cwd=os.path.join(PROJECT_ROOT, 'harry-potter-cloak'),
            creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0
        )
        
        running_processes['cloak'] = process
        
        return jsonify({
            'success': True,
            'message': 'Harry Potter Cloak launched successfully!',
            'pid': process.pid,
            'status': 'running'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/stop/<project>', methods=['POST'])
def stop_project(project):
    """Stop a running project"""
    try:
        if project not in running_processes:
            return jsonify({
                'success': False,
                'message': f'{project} is not running'
            })
        
        proc = running_processes[project]
        
        if proc.poll() is None:
            # Try to terminate gracefully
            if os.name == 'nt':
                # Windows: kill the process tree
                parent = psutil.Process(proc.pid)
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()
            else:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            
            proc.wait(timeout=5)
        
        del running_processes[project]
        
        return jsonify({
            'success': True,
            'message': f'{project} stopped successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/stop/all', methods=['POST'])
def stop_all():
    """Stop all running projects"""
    stopped = []
    errors = []
    
    for name, proc in list(running_processes.items()):
        try:
            if proc.poll() is None:
                if os.name == 'nt':
                    parent = psutil.Process(proc.pid)
                    for child in parent.children(recursive=True):
                        child.terminate()
                    parent.terminate()
                else:
                    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
                proc.wait(timeout=5)
            stopped.append(name)
            del running_processes[name]
        except Exception as e:
            errors.append(f'{name}: {str(e)}')
    
    return jsonify({
        'success': len(errors) == 0,
        'stopped': stopped,
        'errors': errors
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("  Person Re-ID Backend Server")
    print("="*50)
    print(f"  Python: {PYTHON_PATH}")
    print(f"  Project: {PROJECT_ROOT}")
    print("  API Endpoints:")
    print("    GET  /api/status       - Server status")
    print("    POST /api/launch/reid  - Launch Person Re-ID")
    print("    POST /api/launch/cloak - Launch Harry Potter Cloak")
    print("    POST /api/stop/<name>  - Stop a project")
    print("    POST /api/stop/all     - Stop all projects")
    print("="*50 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
