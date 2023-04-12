import semver
import subprocess

# Get the current version from Git
current_version = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()

# Increment the patch version number
new_version = semver.bump_patch(current_version)

# Create a new tag for the new version
subprocess.check_call(['git', 'tag', new_version])

# Push the new tag to the remote repository
subprocess.check_call(['git', 'push', '--tags'])

print('New version:', new_version)
