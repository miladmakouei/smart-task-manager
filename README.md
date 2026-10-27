
# Smart Task Manager

A command-line task management application built with Python.

## Features

- Add tasks with different priority levels
- Assign a unique ID to each task
- Record task creation dates
- Mark tasks as completed
- Filter tasks by status and priority
- Generate task progress reports
- Save and load data using JSON
- Handle common input errors

## Technologies

- Python 3
- JSON
- datetime
- Exception handling

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   `python3 main.py`

## Example

A task contains the following information:

- ID
- Title
- Priority
- Completion status
- Creation date and time

Tasks are stored locally in `tasks.json`, so the information remains available after restarting the application.

## What I Practiced

در این پروژه مفاهیم جدیدی مثل مدیریت خطا با `try/except`،
کار با تاریخ و زمان، فیلتر کردن لیست‌ها و تولید شناسه برای هر کار
را تمرین کردم.

همچنین ذخیره و بازیابی اطلاعات با JSON را که در پروژه قبلی یاد گرفته بودم،
در یک برنامه کاربردی‌تر استفاده کردم.

## Limitations

- Data is stored locally in a JSON file.
- The application does not currently support editing or deleting tasks.
- This is a learning project and does not use a database.

## Future Improvements

- Add task editing and deletion
- Add due dates and overdue task detection
- Export task reports to CSV
- Connect the application to an automation workflow
