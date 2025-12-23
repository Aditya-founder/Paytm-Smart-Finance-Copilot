import { loadUserData } from "../dataLoader/loadUserData.js";
import { loadMerchantData } from "../dataLoader/loadMerchantData.js";

export function buildCopilotContext() {
  const user = loadUserData();
  const merchant = loadMerchantData();

  return {
    user: {
      paymentBehavior: user.paymentBehavior,
    },
    merchant: {
      transactions: merchant.transactions,
    },
  };
}

export function buildReminderContext(upcomingPayment) {
  const user = loadUserData();
  const merchant = loadMerchantData();

  return {
    user: {
      paymentBehavior: user.paymentBehavior,
    },
    merchant: {
      transactions: merchant.transactions,
    },
    payment: upcomingPayment,
  };
}

export default { buildCopilotContext, buildReminderContext };
