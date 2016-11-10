################################################################################
# 				INSTALLING TRANSARIETMATOR TO YOUR SYSTEM					   #
################################################################################

# Change directory to transarietmator root
sudo cp -r transariemator/ /opt/transarietmator

# Grant access
echo "granting access to transarietmator"
sudo chmod a+x /opt/transarietmator/transariemator.py

# Build symlinks for local environment.
echo "Create symlinks to /usr/bin/:"
ln -s /opt/transarietmator/transariemator.py /usr/bin/transarietmator

# Create Login
echo "Installing process done!"