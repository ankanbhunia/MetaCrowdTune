import os
import random

random.seed(1)


class TaskGenerator(object):
    def __init__(self, dataset, data_path, num_of_tasks=10, num_of_instances=5, mode='train'):
        self.dataset = dataset
        self.mode = mode
        self.data_path = os.path.join(data_path)
        self.num_of_instances = num_of_instances
        self.num_of_tasks = num_of_tasks
        self.tasks = [os.path.join(self.data_path, task) for task in os.listdir(self.data_path)]
        random.shuffle(self.tasks)
        self.selected_tasks = self.tasks[:self.num_of_tasks]
        self.train_images, self.validation_images = [], []

        # choosing num_of_instances from each task (scene)
        for task in self.selected_tasks:
            images = [os.path.join(task, img) for img in os.listdir(task) if '.jpg' in img]
            sampled_images = random.sample(images, len(images))
            self.train_images += sampled_images[:self.num_of_instances]
            self.validation_images += sampled_images[self.num_of_instances: (self.num_of_instances * 2)]
