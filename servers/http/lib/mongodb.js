import { MongoClient } from "mongodb"
import {config} from "../config.js"

const client = new MongoClient(config.MONGODB_URI,  { useNewUrlParser: true, useUnifiedTopology: true });

await client.connect();
// set namespace
export const db = client.db(config.MONGODB_DB_NAME);