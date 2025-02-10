import { useState } from 'react';

const Appointment = () => {
    const [appointmentType, setAppointmentType] = useState('online');
    const [doctorId, setDoctorId] = useState('');
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const appointmentData = { appointmentType, doctorId, date, time };

        const response = await fetch('/api/appointments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(appointmentData),
        });

        if (response.ok) {
            // Handle successful appointment scheduling
            alert('Appointment scheduled successfully!');
        } else {
            // Handle error
            alert('Failed to schedule appointment.');
        }
    };

    return (
        <div>
            <h1>Schedule an Appointment</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Appointment Type:
                    <select value={appointmentType} onChange={(e) => setAppointmentType(e.target.value)}>
                        <option value="online">Online</option>
                        <option value="offline">Offline</option>
                    </select>
                </label>
                <br />
                <label>
                    Doctor ID:
                    <input type="text" value={doctorId} onChange={(e) => setDoctorId(e.target.value)} required />
                </label>
                <br />
                <label>
                    Date:
                    <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
                </label>
                <br />
                <label>
                    Time:
                    <input type="time" value={time} onChange={(e) => setTime(e.target.value)} required />
                </label>
                <br />
                <button type="submit">Schedule Appointment</button>
            </form>
        </div>
    );
};

export default Appointment;