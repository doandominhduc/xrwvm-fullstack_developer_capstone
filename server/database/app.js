const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 3050;

app.use(cors());
app.use(express.json()); // Thay cho bodyParser.json() ở các phiên bản cũ

const reviews_data = JSON.parse(fs.readFileSync('./data/reviews.json', 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync('./data/dealerships.json', 'utf8'));

mongoose.connect("mongodb://mongo_db:27017/dealershipsDB");

const Reviews = require('./review');
const Dealerships = require('./dealership');

// Hàm tự động nạp dữ liệu ban đầu vào MongoDB nếu database trống
try {
  Reviews.deleteMany({}).then(() => {
    Reviews.insertMany(reviews_data['reviews']);
  });
  Dealerships.deleteMany({}).then(() => {
    Dealerships.insertMany(dealerships_data['dealerships']);
  });
} catch (error) {
  console.error("Error initializing database:", error);
}

// 1. Endpoint: Lấy toàn bộ danh sách reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching reviews' });
  }
});

// 2. Endpoint: Lấy reviews theo ID của đại lý (dealer_id)
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const documents = await Reviews.find({ dealership: req.params.id });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching reviews for dealer' });
  }
});

// 3. Endpoint: Lấy toàn bộ danh sách dealerships
app.get('/fetchDealers', async (req, res) => {
  try {
    const documents = await Dealerships.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships' });
  }
});

// 4. Endpoint: Lấy các dealership theo bang (state)
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const documents = await Dealerships.find({ state: req.params.state });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships by state' });
  }
});

// 5. Endpoint: Lấy một dealership cụ thể theo ID
app.get('/fetchDealer/:id', async (react, res) => {
  try {
    const document = await Dealerships.findOne({ id: req.params.id });
    if (!document) {
      return res.status(404).json({ error: 'Dealer not found' });
    }
    res.json(document);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealer by id' });
  }
});

// 6. Endpoint: Thêm mới một review (POST request)
app.post('/insert_review', async (req, res) => {
  try {
    const data = req.body;
    const documents = await Reviews.find().sort({ id: -1 });
    let new_id = documents.length > 0 ? documents[0].id + 1 : 1;

    const review = new Reviews({
      id: new_id,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

app.listen(port, () => {
  console.log(`Express server is running on port ${port}`);
});