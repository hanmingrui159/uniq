import uuid
import datetime
import time
import logging


def get_uuid4_hex():
    return uuid.uuid4().hex

def snowid_generator(worker_id, data_center_id, sleep=lambda x: time.sleep(x/1000.0)):
    log = logging.getLogger(__name__)

    twepoch = 1262275200000
    worker_id_bits = 5
    data_center_id_bits = 5
    max_worker_id = -1 ^ (-1 << worker_id_bits)
    max_data_center_id = -1 ^ (-1 << data_center_id_bits)
    sequence_bits = 12
    worker_id_shift = sequence_bits
    data_center_id_shift = sequence_bits + worker_id_bits
    timestamp_left_shift = sequence_bits + worker_id_bits + data_center_id_bits
    sequence_mask = -1 ^ (-1 << sequence_bits)

    assert worker_id >= 0 and worker_id <= max_worker_id
    assert data_center_id >= 0 and data_center_id <= max_data_center_id

    last_timestamp = -1
    sequence = 0

    while True:
        timestamp = int(time.time()*1000)

        if last_timestamp > timestamp:
            log.warning(
                "clock is moving backwards. waiting until %i" % last_timestamp)
            sleep(last_timestamp-timestamp)
            continue

        if last_timestamp == timestamp:
            sequence = (sequence + 1) & sequence_mask
            if sequence == 0:
                log.warning("sequence overrun")
                sequence = -1 & sequence_mask
                sleep(1)
                continue
        else:
            sequence = 0

        last_timestamp = timestamp

        yield (
            ((timestamp-twepoch) << timestamp_left_shift) |
            (data_center_id << data_center_id_shift) |
            (worker_id << worker_id_shift) |
            sequence)


def test_get_uuid4_hex():
    i = get_uuid4_hex()
    print(i)


def test_snowid_generator():
    s = snowid_generator(1,1)
    for k in range(1,10):
        time.sleep(0.3)
        new_id = next(s)
        print(new_id)

if __name__ == '__main__':
    test_get_uuid4_hex()
    # test_snowid_generator()
    