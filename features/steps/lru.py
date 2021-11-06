from behave import *


class Lru:
    def __init__(self, max_length=5):
        self.max_length = max_length
        self.list = []

    def size(self):
        return len(self.list)

    def add(self, file_name):
        if file_name in self.list:
            del self.list[self.list.index(file_name)]

        self.list = [file_name] + self.list
        self.list = self.list[:self.max_length]

    def get(self, index):
        return self.list[index]


@when(u'a new list is created')
def step_impl(context):
    context.list = Lru()


@then(u'the list is empty')
def step_impl(context):
    assert context.list.size() == 0


@given(u'an empty list exists')
def step_impl(context):
    context.list = Lru()


@when(u'we open a new file')
def step_impl(context):
    context.last_file_name = 'dummy_file'
    context.list.add(context.last_file_name)


@then(u'the list has one element')
def step_impl(context):
    assert context.list.size() == 1


@then(u'the new file is first')
def step_impl(context):
    assert context.list.get(0) == context.last_file_name, context.list.get(0)


@given(u'not empty list exists')
def step_impl(context):
    context.list = Lru()
    context.previous_file_name = 'file1'
    context.list.add('file1')


@when(u'new file is opened')
def step_impl(context):
    context.last_file_name = 'new_file'
    context.list.add('new_file')


@then(u'the rest of elements go to next positions')
def step_impl(context):
    assert context.list.get(0) == context.last_file_name, context.list.get(0)
    assert context.list.get(1) == context.previous_file_name, context.list.get(1)


@given(u'a list with 5 elements exists')
def step_impl(context):
    context.list = Lru()
    files_to_add = ['file1', 'file2', 'file3', 'file4']
    context.files_that_should_stay = files_to_add
    context.previous_file_name = 'file5'

    for file in files_to_add:
        context.list.add(file)

    context.list.add('file5')


@then(u'the oldest one is deleted from the list')
def step_impl(context):
    assert context.list.list == ['new_file', 'file5', 'file4', 'file3', 'file2'], context.list.list


@given(u'a list with three elements')
def step_impl(context):
    context.list = Lru()
    context.list.add('file1')
    context.list.add('file2')
    context.list.add('file3')


@when(u'we open the second file from the list again')
def step_impl(context):
    second_element = context.list.get(1)
    context.list.add(second_element)


@then(u'the file is moved to the first place on the list')
def step_impl(context):
    assert context.list.list == ['file2', 'file3', 'file1']
