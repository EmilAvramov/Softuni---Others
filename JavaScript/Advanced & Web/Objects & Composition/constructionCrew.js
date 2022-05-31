function worker({ weight, experience, levelOfHydrated, dizziness }) {
    const reqWater = 0.1 * weight * experience;
    let modified = {};
    if (dizziness) {
        levelOfHydrated += reqWater;
        dizziness = false;
    }

    modified.weight = weight;
    modified.experience = experience;
    modified.levelOfHydrated = levelOfHydrated;
    modified.dizziness = dizziness;

    return modified;
}

worker({ weight: 80, experience: 1, levelOfHydrated: 0, dizziness: true });
worker({ weight: 95, experience: 3, levelOfHydrated: 0, dizziness: false });
