Perfect, Vikash! Let’s now:

1. ✅ Add **Git tagging/versioning**
2. 🛠️ Add a `Makefile` to run scripts easily
3. ⚙️ Set up **GitHub Actions** for Python script linting (with `flake8`)

---

## ✅ 1. Git Versioning with Tags

Use tags to mark releases or stable checkpoints.

```bash
git tag -a v1.0 -m "Initial version of Linux and AWS scripts"
git push origin v1.0
```

To list tags later:

```bash
git tag
```

---

## 🛠️ 2. `Makefile` for Convenience

Create a file named `Makefile` in the root of your repo:

```Makefile
.PHONY: help lint list-instances cleanup-ebs s3-sync

help:
	@echo "Available targets:"
	@echo "  lint             - Run flake8 linting on python scripts"
	@echo "  list-instances   - Run EC2 instance listing script"
	@echo "  cleanup-ebs      - Run EBS cleanup script"
	@echo "  s3-sync SRC=dir BUCKET=name - Sync folder to S3"

lint:
	flake8 python/

list-instances:
	python python/list_ec2_instances.py

cleanup-ebs:
	python python/ebs_cleanup.py

s3-sync:
	bash bash/aws_s3_sync.sh $(SRC) $(BUCKET)
```

Now you can run:

```bash
make list-instances
make cleanup-ebs
make s3-sync SRC=./data BUCKET=my-bucket-name
```

---

## ⚙️ 3. GitHub Actions for Python Linting

Create the following file:

```bash
mkdir -p .github/workflows
```

Then create `.github/workflows/python-lint.yml`:

```yaml
name: Lint Python Scripts

on:
  push:
    paths:
      - 'python/**.py'
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install flake8
        run: pip install flake8

      - name: Run flake8
        run: flake8 python/
```

Push the workflow file:

```bash
git add .github/
git commit -m "Add GitHub Actions workflow for Python linting"
git push
```

Now GitHub will **automatically lint Python scripts** on every push or pull request.

---

## ✅ Summary

You now have:

* ✅ Git versioning via `git tag`
* ✅ A clean `Makefile` to simplify running scripts
* ✅ GitHub Actions CI for linting Python

---

Would you like to:

* Add **ShellCheck** for Bash script linting too?
* Setup `pre-commit` hooks locally?
* Add Terraform or Lambda script templates next?

Happy to extend further.
#*********************************************************************************************
Here’s a **basic guide to `Makefile`** for scripting use cases — perfect for your Bash & Python automation repo.

---

## 🔧 What is a Makefile?

A `Makefile` is a file used by the `make` command to automate tasks with simple shell commands. Originally for compiling C code, it’s now widely used to:

* Run scripts
* Lint code
* Sync files
* Automate repetitive CLI tasks

---

## 🗂️ Simple Structure of a Makefile

```makefile
target-name:
    shell-command-to-run
```

> 💡 Use a **tab**, not spaces, before the command under the target.

---

## ✅ Example: Basic Makefile for Your Scripts

```makefile
# List available tasks
help:
	@echo "Usage: make <target>"
	@echo "Available targets:"
	@echo "  list-instances     List EC2 instances using Python"
	@echo "  cleanup-ebs        Delete unused EBS volumes"
	@echo "  s3-sync            Sync a folder to S3 bucket (SRC, BUCKET required)"
	@echo "  lint               Lint Python files using flake8"

# Run EC2 instance listing script
list-instances:
	python python/list_ec2_instances.py

# Run EBS cleanup script
cleanup-ebs:
	python python/ebs_cleanup.py

# Lint all Python scripts
lint:
	flake8 python/

# Sync local folder to S3
s3-sync:
	bash bash/aws_s3_sync.sh $(SRC) $(BUCKET)
```

---

## 🏃 How to Use It

```bash
make help                  # See available commands
make list-instances        # Run EC2 instance lister
make cleanup-ebs           # Run EBS volume cleanup
make lint                  # Lint Python code
make s3-sync SRC=./data BUCKET=my-bucket-name  # Sync data folder to S3
```

---

## 🔁 Variables (Optional)

You can define and reuse variables like this:

```makefile
SCRIPTS_DIR=python

lint:
	flake8 $(SCRIPTS_DIR)/
```

---

## ⚠️ Common Mistakes

* Always use a **tab**, not spaces, before the command under a target.
* Avoid colons `:` in variable values unless quoting.
* Always check indentation if `make` gives weird errors.

---

Would you like a Makefile template for:

* Terraform commands?
* Lambda build/deploy flow?
* Docker workflow?

Let me know — I can tailor it to your stack.

#*********************************************************************************************
# Scripts Repository Documentation
# =========================
# This document provides an overview of the scripts available in this repository, including their purpose and usage.

## 🖥️ Linux Scripts (`bash/`)
# These scripts are designed for various Linux system management tasks.
- `disk_usage_report.sh`: Generates a report of disk usage per mount point.
- `aws_s3_sync.sh`: Syncs a local directory to an AWS S3 bucket.
- `ec2_instance_report.sh`: Fetches a summary of EC2 instances in the AWS account.
## ☁️ AWS Scripts (`python/`)
# These Python scripts interact with AWS services for automation and management.
- `list_ec2_instances.py`: Lists information about EC2 instances in the AWS account.
- `list_s3_buckets.py`: Lists all S3 buckets in the AWS account.
- `ebs_cleanup.py`: Deletes unused EBS volumes to free up resources.
## Usage
# To use these scripts, follow the instructions below:
## Linux Scripts
### Disk Usage Report
Run the disk usage report script to see how much space each mount point is using:

```bash
bash bash/disk_usage_report.sh
```
### AWS S3 Sync
To sync a local directory to an S3 bucket, use the following command:

```bash
bash bash/aws_s3_sync.sh <SRC> <BUCKET>
```
Replace `<SRC>` with the local directory path and `<BUCKET>` with the S3 bucket name.
### EC2 Instance Report
To fetch a summary of EC2 instances, run:

```bash
bash bash/ec2_instance_report.sh
```
## AWS Scripts
### List EC2 Instances
To list EC2 instances, execute the following command:

```bash
python python/list_ec2_instances.py
```
### List S3 Buckets
To list all S3 buckets, run:

```bash
python python/list_s3_buckets.py
```
### EBS Cleanup
To delete unused EBS volumes, run:

```bash
python python/ebs_cleanup.py
```
## Requirements
```bash
pip install -r requirements.txt
```
## Contributing
If you would like to contribute to this repository, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.
## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
#*********************************************************************************************
#*********************************************************************************************
# This is a simple documentation file for the scripts repository.
# Scripts Repository
# =========================
# A collection of useful Bash and Python scripts for Linux system management and AWS automation.
### 🖥️ Linux Scripts (`bash/`
# These scripts are designed for various Linux system management tasks.
- `disk_usage_report.sh`: Shows disk usage per mount point.
- `aws_s3_sync.sh`: Syncs a local directory to an AWS S3 bucket.
- `ec2_instance_report.sh`: Fetches a summary of EC2 instances in the AWS account.
### ☁️ AWS Scripts (`python/`
# These Python scripts interact with AWS services for automation and management.
- `list_ec2_instances.py`: Lists information about EC2 instances in the AWS account.
- `list_s3_buckets.py`: Lists all S3 buckets in the AWS account.
- `ebs_cleanup.py`: Deletes unused EBS volumes to free up resources.
## Usage
# To use these scripts, follow the instructions below:
### Linux Scripts
#### Disk Usage Report
Run the disk usage report script to see how much space each mount point is using:

```bash
bash bash/disk_usage_report.sh
```
#### AWS S3 Sync
To sync a local directory to an S3 bucket, use the following command:

```bash
bash bash/aws_s3_sync.sh <SRC> <BUCKET>
```
Replace `<SRC>` with the local directory path and `<BUCKET>` with the S3 bucket name.
#### EC2 Instance Report
To fetch a summary of EC2 instances, run:

```bash
bash bash/ec2_instance_report.sh
```
### AWS Scripts
#### List EC2 Instances
To list EC2 instances, execute the following command:

```bash
python python/list_ec2_instances.py
```
#### List S3 Buckets
To list all S3 buckets, run:

```bash
python python/list_s3_buckets.py
```
#### EBS Cleanup
To delete unused EBS volumes, run:

```bash
python python/ebs_cleanup.py
```
## Requirements
To run the Python scripts, you need to install the required dependencies. Use the following command:

```bash
pip install -r requirements.txt
```
## Contributing

If you would like to contribute to this repository, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.
## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
#*********************************************************************************************
#*********************************************************************************************
