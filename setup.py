#!/usr/bin/env python3
from modules.interactions import *
from subprocess import call
import sys, getpass, os
devnull = open(os.devnull, 'w')


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
        call(["git", "clone", "{}".format(git_repo)], cwd="/home/{}/".format(getpass.getuser()))

        # get repo name
        repo_name = str(input("\nPlease enter the name of the django project repo root folder: "))
        # django repo project folder name
        project_folder = str(
            input(
                "Please enter the name of the folder containing settings.py within your django project: {}/".format(
                    repo_name
                )
            )
        )
        use_mysql = str(input("\nDo you wish to use mysql as your django db backend (defaults db.sqlite)? [ y/n ]"))
        if use_mysql.lower() == 'y':
            mysql_password = str(input("\nPlease enter a mysql root user password: "))
            mysql_database = str(input("\nPlease enter a name for your database: "))


        # ./install_pre_reqs.sh
        call(['sudo', './scripts/install_pre_reqs.sh'],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # ./update.sh
        call(['sudo', './scripts/update.sh'],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # ./raise_firewall.sh
        call(['sudo', './raise_firewall.sh'], cwd="/home/{}/djangodeploy".format(getpass.getuser()))



        # ./install_mysql.sh
        call(['sudo', './scripts/install_mysql.sh', mysql_password, mysql_database], cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # if str(input("{} [ y/n ]".format("Would you like to install redis?"))).lower() == 'y':
        #     # ./install_redis.sh
        #     call(['sudo', './install_redis.sh'], shell=True, cwd="~/")
        #
        # if str(input("{} [ y/n ]".format("Would you like to install node?"))).lower() == 'y':
        #     # ./install_node.sh
        #     call(['sudo', './install_node.sh'], shell=True, cwd="~/")

        # ./install_virtualenv.sh
        call(['sudo', './scripts/install_virtualenv.sh', getpass.getuser()], cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # ./install_django_project.sh
        call(['sudo', './scripts/install_django_project.sh', repo_name],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # django setup database backend
        if use_mysql.lower() == 'y':
            call(['sudo', './scripts/django_setup_mysql.sh', repo_name, project_folder, mysql_password, mysql_database],
                 cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # django migrate
        call(['sudo', './scripts/django_migrate.sh', repo_name],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # django cors setup
        call(['sudo', './scripts/django_cors_setup.sh', repo_name, project_folder],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()))

        # deploy
        call(['sudo', './scripts/install_deploy.sh', getpass.getuser(), repo_name, project_folder],
             cwd="/home/{}/djangodeploy".format(getpass.getuser()),)

        # status report
        call(['sudo', './scripts/status_report.sh'], cwd="/home/{}/djangodeploy".format(getpass.getuser()))

    else:
        sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
