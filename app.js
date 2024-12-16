const express = require("express");
const { Storage } = require("@google-cloud/storage");

const app = express();
const storage = new Storage();

app.get("/", async (req, res) => {
  console.log("Received a request to list bucket contents.");

  const bucketName = "stt-test-chronicle"; // Replace with your GCP bucket name
  try {
    console.log(`Accessing bucket: ${bucketName}`);
    const [files] = await storage.bucket(bucketName).getFiles();
    console.log("Files retrieved successfully:", files.map(file => file.name));
    res.json({ bucket: bucketName, files: files.map(file => file.name) });
  } catch (error) {
    console.error("Error accessing bucket:", error);
    res.status(500).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
