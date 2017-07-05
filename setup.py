#!/usr/bin/env python3
from modules.interactions import *
from subprocess import call
import sys, getpass, os
devnull = open(os.devnull, 'w')


# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def main():
    # print banner, website and github information.
    print("{}\n{}\n{}\n{}\n".format(
        get_version(),
        get_banner(),
        get_website(),
        get_github(),
    ))

    if str(input("{} [ y/n ] ".format(get_confirmation()))).lower() == 'y':

        # clone repo
        git_repo = str(input("Enter in the repo to clone: "))
        print_progress_bar(0, 9, prefix='Progress:', suffix='Complete | Cloning Repo', length=50)
        call(["git", "clone", "{}".format(git_repo)], cwd="/home/{}/".format(getpass.getuser()))

        # get repo name
        repo_name = str(input("Please enter the name of the django project repo root folder: "))

        # django repo project folder name
        project_folder = str(
            input("Please enter the name of the folder containing settings.py within your django project: ")
        )

        print_progress_bar(1, 9, prefix='Progress:', suffix='Complete | Installing system pre-requisites', length=50)
        # ./install_pre_reqs.sh
        call(['sudo', './scripts/install_pre_reqs.sh'],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # ./update.sh
        call(['sudo', './scripts/update.sh'],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        print_progress_bar(2, 9, prefix='Progress:', suffix='Complete | Raising firewall', length=50)
        # ./raise_firewall.sh
        call(['sudo', './raise_firewall.sh'], cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        print_progress_bar(3, 9, prefix='Progress:', suffix='Complete | Installing mysql', length=50)

        mysql_password = str(input("\nPlease enter a mysql root user password: "))
        mysql_database = str(input("\nPlease enter a name for your database: "))
        # ./install_mysql.sh
        call(['sudo', './scripts/install_mysql.sh', mysql_password, mysql_database], cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # if str(input("{} [ y/n ]".format("Would you like to install redis?"))).lower() == 'y':
        #     # ./install_redis.sh
        #     call(['sudo', './install_redis.sh'], shell=True, cwd="~/")
        #
        # if str(input("{} [ y/n ]".format("Would you like to install node?"))).lower() == 'y':
        #     # ./install_node.sh
        #     call(['sudo', './install_node.sh'], shell=True, cwd="~/")

        print_progress_bar(4, 9, prefix='Progress:', suffix='Complete | Raising firewall', length=50)
        # ./install_virtualenv.sh
        call(['sudo', './scripts/install_virtualenv.sh', getpass.getuser()], cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        print_progress_bar(5, 9, prefix='Progress:', suffix='Complete | Installing django project', length=50)
        # ./install_django_project.sh
        call(['sudo', './scripts/install_django_project.sh', repo_name],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        print_progress_bar(6, 9, prefix='Progress:', suffix='Complete | Setting up django database', length=50)
        # django setup database backend
        call(['sudo', './scripts/django_setup_mysql.sh', repo_name, project_folder, mysql_password, mysql_database],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        print_progress_bar(7, 9, prefix='Progress:', suffix='Complete | Migrating django', length=50)
        # django migrate
        call(['sudo', './scripts/django_migrate.sh', repo_name],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # django cors setup
        print("please add 'SERVERIPADDRESS' as a placeholder as is into the CORS and Allowed_hosts.")
        print_progress_bar(8, 9, prefix='Progress:', suffix='Complete | Setting up django CORS', length=50)
        call(['sudo', './scripts/django_cors_setup.sh', repo_name, project_folder],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # deploy
        print_progress_bar(9, 9, prefix='Progress:', suffix='Complete | deploying gunicorn and nginx', length=50)
        call(['sudo', './scripts/install_deploy.sh', getpass.getuser(), repo_name, project_folder],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()),)

        # status report
        call(['sudo', './scripts/status_report.sh'], shell=True, cwd="/home/{}/djangodeploy".format(getpass.getuser()))

    else:
        sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
