import userProfile from "../../data/users/user_profile.json" with { type: "json" };
import userPreferences from "../../data/users/user_preferences.json" with { type: "json" };
import paymentBehavior from "../../data/behavior/payment_behavior.json" with { type: "json" };

export function loadUserData() {
  return {
    profile: userProfile,
    preferences: userPreferences,
    paymentBehavior,
  };
} 
export default loadUserData;
