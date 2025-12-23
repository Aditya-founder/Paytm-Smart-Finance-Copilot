import e from "express";
import merchantProfile from "../../data/merchants/merchant_profile.json" with { type: "json" };
import merchantTransactions from "../../data/merchants/merchant_transaction.json" with { type: "json" };



export function loadMerchantData() {
  return {
    profile: merchantProfile,
    transactions: merchantTransactions,
  };
}
export default loadMerchantData;
