import time


class AdaptiveController:

    H_GREEN = "H_GREEN"
    H_YELLOW = "H_YELLOW"

    V_GREEN = "V_GREEN"
    V_YELLOW = "V_YELLOW"

    def __init__(self):

        self.phase = self.H_GREEN

        self.last_change = time.time()

        self.min_green = 5
        self.max_green = 12

        self.yellow_time = 2

    # -----------------------------

    def calculate_score(self, queue, waiting):

        if queue == 0:
            return 0

        average_wait = sum(waiting) / len(waiting) if waiting else 0

        return queue * 2 + average_wait * 0.3

    # -----------------------------

    def update(self,
               horizontal_queue,
               horizontal_waiting,
               vertical_queue,
               vertical_waiting):

        now = time.time()

        elapsed = now - self.last_change

        h_score = self.calculate_score(
            horizontal_queue,
            horizontal_waiting
        )

        v_score = self.calculate_score(
            vertical_queue,
            vertical_waiting
        )

        # ----------------------------
        # Horizontal Green
        # ----------------------------

        if self.phase == self.H_GREEN:

            if elapsed >= self.max_green:

                self.phase = self.H_YELLOW
                self.last_change = now

            elif elapsed >= self.min_green:

                if v_score > h_score + 2:

                    self.phase = self.H_YELLOW
                    self.last_change = now

        # ----------------------------
        # Horizontal Yellow
        # ----------------------------

        elif self.phase == self.H_YELLOW:

            if elapsed >= self.yellow_time:

                self.phase = self.V_GREEN
                self.last_change = now

        # ----------------------------
        # Vertical Green
        # ----------------------------

        elif self.phase == self.V_GREEN:

            if elapsed >= self.max_green:

                self.phase = self.V_YELLOW
                self.last_change = now

            elif elapsed >= self.min_green:

                if h_score > v_score + 2:

                    self.phase = self.V_YELLOW
                    self.last_change = now

        # ----------------------------
        # Vertical Yellow
        # ----------------------------

        elif self.phase == self.V_YELLOW:

            if elapsed >= self.yellow_time:

                self.phase = self.H_GREEN
                self.last_change = now

        return self.phase