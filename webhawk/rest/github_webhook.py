from rest.api_errors import InvalidUsage
from rest.webhook_base import WebHookBase

__author__ = "Dimi Balaouras"
__copyright__ = "Copyright 2016, Stek.io"
__license__ = "Apache License 2.0, see LICENSE for more details."


class GithubWebHook(WebHookBase):
    """
    RESTful Resource for the Github Webhook
    """
    resource_name = "github"

    def create_task(self, input):
        """
        Creates a new build task using the input (usually a POST Payload)
        """

        # Get the task manager
        task_manager = self._context.get("task_manager")

        try:
            repository_name = input['repository']['name']
            branch_name = input['ref'].split('/')[2]
            vcs = "git"
        except KeyError:
            raise InvalidUsage("Invalid payload: %s" % str(input))

        # Construct the new task
        new_task = task_manager.create_new_task(repository_name=repository_name, branch_name=branch_name, vcs=vcs)

        return new_task
