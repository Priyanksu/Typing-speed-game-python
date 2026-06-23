# ⚡ Speed Finger - Retro Tkinter Typing Game ⌨️

A fast-paced, desktop-based speed typing game built using Python and the Tkinter GUI library. Test your typing speed (WPM) and accuracy against a 60-second ticking clock with dynamic random word generation!

## 🚀 Key Features

* **Instant Verification:** Evaluates input accuracy instantly when you hit the `<Return>` (Enter) key.
* **Live Countdown Timer:** Uses Tkinter's internal asynchronous event looping (`.after()`) to handle precise 1-second clock decrements without freezing the UI.
* **Performance Metrics Dashboard:** Automatically calculates and displays your final Net Speed in Words Per Minute (WPM) and exact fractional accuracy percentage.
* **Built-in Session Reset:** Integrated popup prompts allow you to quickly cycle back and restart your practice session without restarting the script.

## 🛠️ System Architecture & Mechanics

* **The GUI Engine:** Built using Python's native `tkinter` layout hooks.
* **Asynchronous Timing Engine:** Operates entirely via `Time_label.after(1000, ch_time)` to avoid locking execution scopes during countdown loops.
* **Event Interception Engine:** Binds the `<Return>` key to the main input evaluation layout block.
