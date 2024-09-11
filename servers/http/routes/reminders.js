import {Router} from "express"
import { db } from "../lib/mongodb.js"

export const remindersRoutes = Router()

// CREATE: Add a new item
remindersRoutes.post("/", async (req, res) => {
  const collection = db.collection('reminders-eloi-buil-cuadrat-3000')
  try {
    const newItem = req.body;
    const result = await collection.insertOne(newItem);
    res.status(201).send(result.ops[0]); // Return the inserted item
  } catch (err) {
    res.status(500).send({ error: 'Failed to add item' });
  }
});

// READ: Get all items
remindersRoutes.get("/", async (req, res) => {
  try {
    const items = await collection.find().toArray();
    res.status(200).send(items);
  } catch (err) {
    res.status(500).send({ error: 'Failed to get items' });
  }
});

// READ: Get a single item by ID
remindersRoutes.get("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const item = await collection.findOne({ _id: new ObjectId(id) });
    if (item) {
      res.status(200).send(item);
    } else {
      res.status(404).send({ error: 'Item not found' });
    }
  } catch (err) {
    res.status(500).send({ error: 'Failed to get item' });
  }
});

// UPDATE: Update an item by ID
remindersRoutes.put("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const updatedItem = req.body;
    const result = await collection.updateOne(
      { _id: new ObjectId(id) },
      { $set: updatedItem }
    );
    if (result.matchedCount > 0) {
      res.status(200).send({ message: 'Item updated' });
    } else {
      res.status(404).send({ error: 'Item not found' });
    }
  } catch (err) {
    res.status(500).send({ error: 'Failed to update item' });
  }
})

// DELETE: Delete an item by ID
remindersRoutes.delete("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const result = await collection.deleteOne({ _id: new ObjectId(id) });
    if (result.deletedCount > 0) {
      res.status(200).send({ message: 'Item deleted' });
    } else {
      res.status(404).send({ error: 'Item not found' });
    }
  } catch (err) {
    res.status(500).send({ error: 'Failed to delete item' });
  }
})