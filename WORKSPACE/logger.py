import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage


def my_function():
    logging.debug('This is a debug message.')
    logging.info('This is an informational message.')
    logging.warning('This is a warning message.')
    logging.error('This is an error message.')


if __name__ == "__main__":
    my_function()
