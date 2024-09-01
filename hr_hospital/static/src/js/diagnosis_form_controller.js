/** @odoo-module **/

import { useState, useEffect } from "@odoo/owl";

export const DiagnosisFormController = (env) => {
    const state = useState({
        isIntern: false, // Track whether the selected doctor is an intern
    });

    // Effect to update isIntern whenever doctor_id changes
    useEffect(() => {
        const doctorField = env.model.fields.doctor_id;
        const handleFieldChange = () => {
            const selectedDoctor = env.model.get('doctor_id');
            if (selectedDoctor && selectedDoctor.is_intern) {
                state.isIntern = true;
            } else {
                state.isIntern = false;
            }
        };

        doctorField.on('change', handleFieldChange);

        // Cleanup listener on component destroy
        return () => {
            doctorField.off('change', handleFieldChange);
        };
    }, [env.model.fields.doctor_id]);

    return { state };
};