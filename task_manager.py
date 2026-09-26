def get_statistics(self) -> dict:
     """Get task statistics by status."""
     return {
         "total": self.count_tasks(),
         "todo": self.count_by_status(TaskStatus.TODO),
         "in_progress": self.count_by_status(TaskStatus.IN_PROGRESS),
         "done": self.count_by_status(TaskStatus.DONE),
     }