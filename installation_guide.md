# 🛠️ AWS CLI & Docker Installation Guide

This guide covers the installation of AWS CLI and Docker on different operating systems.

---

## 🐳 Docker Installation

### **Windows**

#### Option 1: Docker Desktop (Recommended)

1. **System Requirements:**
   - Windows 10 64-bit: Pro, Enterprise, or Education (Build 19041+)
   - OR Windows 11 64-bit: Home or Pro (Build 22000+)
   - WSL 2 feature enabled

2. **Enable WSL 2:**
   ```powershell
   # Run in PowerShell as Administrator
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   
   # Restart computer, then set WSL 2 as default
   wsl --set-default-version 2
   ```

3. **Download and Install:**
   - Visit: https://www.docker.com/products/docker-desktop/
   - Download "Docker Desktop for Windows"
   - Run the installer
   - Restart when prompted
   - Launch Docker Desktop

4. **Verify Installation:**
   ```cmd
   docker --version
   docker run hello-world
   ```

### **macOS**

#### Option 1: Docker Desktop (Recommended)

1. **Download Docker Desktop:**
   - Visit: https://www.docker.com/products/docker-desktop/
   - Click "Download for Mac"
   - Choose your chip type (Intel or Apple Silicon)

2. **Install Docker Desktop:**
   - Double-click the downloaded `.dmg` file
   - Drag Docker to Applications folder
   - Launch Docker from Applications
   - Follow the setup wizard

3. **Verify Installation:**
   ```bash
   docker --version
   docker run hello-world
   ```

#### Option 2: Homebrew

```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Docker
brew install docker
brew install docker-compose

# Install Docker Desktop (GUI)
brew install --cask docker
```

### **Linux (Ubuntu/Debian)**

#### Method 1: Official Docker Repository (Recommended)

```bash
# 1. Update package index
sudo apt-get update

# 2. Install prerequisite packages
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 3. Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Update package index again
sudo apt-get update

# 6. Install Docker Engine
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# 7. Add your user to docker group
sudo usermod -aG docker $USER

# 8. Reload group membership
newgrp docker
```

#### Method 2: Convenience Script

```bash
# Download and run Docker's convenience script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

#### Method 3: GitHub Codespaces

```bash
# Install Docker in Codespaces
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Start Docker service
sudo service docker start

# Test installation
docker --version
docker run hello-world
```

### **Verify Docker Installation**

```bash
# Check Docker version
docker --version

# Check Docker Compose version
docker compose version

# Test with hello-world
docker run hello-world

# Check system info
docker system info
```

---

## ☁️ AWS CLI Installation

### **Windows**

#### Method 1: MSI Installer (Recommended)

1. **Download the MSI installer:**
   - Visit: https://awscli.amazonaws.com/AWSCLIV2.msi
   - Download the file

2. **Run the installer:**
   - Double-click the downloaded MSI file
   - Follow the installation wizard
   - Accept the default settings

3. **Verify installation:**
   ```cmd
   aws --version
   ```

#### Method 2: Using pip

```cmd
# Install using pip
pip install awscli

# Verify installation
aws --version
```

### **macOS**

#### Method 1: PKG Installer (Recommended)

```bash
# Download and install
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

# Verify installation
aws --version
```

#### Method 2: Homebrew

```bash
# Install using Homebrew
brew install awscli

# Verify installation
aws --version
```

### **Linux (Ubuntu/Debian)**

#### Method 1: Official Installer (Recommended)

```bash
# Download AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Install unzip if needed
sudo apt update
sudo apt install unzip

# Extract and install
unzip awscliv2.zip
sudo ./aws/install

# Verify installation
aws --version

# Clean up
rm -rf awscliv2.zip aws/
```

#### Method 2: Using pip

```bash
# Install using pip
pip install awscli

# Verify installation
aws --version
```

#### Method 3: GitHub Codespaces

```bash
# Quick install for Codespaces
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt update && sudo apt install unzip -y
unzip awscliv2.zip
sudo ./aws/install
rm -rf awscliv2.zip aws/

# Verify installation
aws --version
```

### **Verify AWS CLI Installation**

```bash
# Check AWS CLI version
aws --version

# Expected output:
# aws-cli/2.x.x Python/3.x.x Linux/x.x.x exe/x86_64
```

---

## 🔧 Post-Installation Setup

### **Configure AWS CLI**

```bash
# Configure AWS CLI with your credentials
aws configure

# You'll be prompted for:
# AWS Access Key ID: [Your Access Key]
# AWS Secret Access Key: [Your Secret Key]
# Default region name: us-east-1
# Default output format: json
```

### **Test AWS CLI**

```bash
# Test AWS CLI configuration
aws sts get-caller-identity

# Expected output:
{
    "UserId": "AIDAIOSFODNN7EXAMPLE",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/your-username"
}
```

### **Test Docker**

```bash
# Test Docker with a simple container
docker run hello-world

# Expected output:
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```

---

## 🚀 Install EB CLI (Bonus)

### **All Platforms**

```bash
# Install EB CLI using pip
pip install awsebcli

# Verify installation
eb --version

# Expected output:
# EB CLI 3.x.x (Python 3.x.x)
```

---

## ✅ Installation Verification Script

Save this as `verify-installation.sh`:

```bash
#!/bin/bash

echo "🔍 Checking Installation Status"
echo "==============================="

# Check Docker
echo "1. Docker:"
if command -v docker &> /dev/null; then
    echo "   ✅ Docker installed: $(docker --version)"
    if docker ps &> /dev/null; then
        echo "   ✅ Docker daemon running"
    else
        echo "   ⚠️  Docker daemon not running"
    fi
else
    echo "   ❌ Docker not installed"
fi

# Check AWS CLI
echo "2. AWS CLI:"
if command -v aws &> /dev/null; then
    echo "   ✅ AWS CLI installed: $(aws --version)"
else
    echo "   ❌ AWS CLI not installed"
fi

# Check EB CLI
echo "3. EB CLI:"
if command -v eb &> /dev/null; then
    echo "   ✅ EB CLI installed: $(eb --version)"
else
    echo "   ⚠️  EB CLI not installed (optional)"
fi

# Test Docker
echo "4. Testing Docker:"
if docker run --rm hello-world &> /dev/null; then
    echo "   ✅ Docker working correctly"
else
    echo "   ❌ Docker test failed"
fi

# Test AWS CLI
echo "5. Testing AWS CLI:"
if aws sts get-caller-identity &> /dev/null; then
    echo "   ✅ AWS CLI configured and working"
else
    echo "   ⚠️  AWS CLI not configured (run 'aws configure')"
fi

echo "==============================="
echo "🎉 Installation check complete!"
```

Run the verification script:

```bash
chmod +x verify-installation.sh
./verify-installation.sh
```

---

## 🔧 Troubleshooting

### **Docker Issues**

#### Permission Denied (Linux)
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Or run with sudo temporarily
sudo docker run hello-world
```

#### Docker Daemon Not Running
```bash
# Start Docker daemon (Linux)
sudo systemctl start docker
sudo systemctl enable docker

# Start Docker Desktop (macOS/Windows)
# Launch Docker Desktop application
```

### **AWS CLI Issues**

#### Command Not Found
```bash
# Check PATH
echo $PATH

# Reinstall AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --update
```

#### Access Denied
```bash
# Check credentials
aws sts get-caller-identity

# Reconfigure if needed
aws configure
```

