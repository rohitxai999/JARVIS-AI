from app.core.jarvis import Jarvis


def test_jarvis_autonomous_system_status():

    jarvis = Jarvis()

    response = jarvis.chat(
        "Check the system status including CPU and memory"
    )

    assert response
    assert "Task completed successfully." in response


def test_jarvis_existing_time_command():

    jarvis = Jarvis()

    response = jarvis.chat(
        "What time is it?"
    )

    assert response
    assert "current time" in response.lower()


def test_jarvis_empty_message():

    jarvis = Jarvis()

    response = jarvis.chat("")

    assert response == "Please enter a message."