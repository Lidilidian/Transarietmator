################################################################################
# 			INSTALLING CEKSIPO TO YOUR SYSTEM	  	       #
################################################################################

# Change directory to ceksipo root
sudo cp -r transariemator/ /opt/ceksipo

# Grant access
echo "granting access to ceksipo..."
sudo chmod a+x /opt/ceksipo/ceksipo.py

# Build symlinks for local environment.
echo "Create symlinks to /usr/bin/:"
ln -s /opt/ceksipo/transariemator.py /usr/bin/ceksipo

# Create Login
echo "Installing process done!"