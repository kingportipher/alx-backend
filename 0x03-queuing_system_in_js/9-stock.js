import express from 'express';
import redis from 'redis';
import util from 'util';

// Connect to Redis client
const client = redis.createClient();
client.on('connect', () => {
    console.log('Connected to Redis server');
}).on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

// List of products
const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Function to get an item by its ID
function getItemById(id) {
    return listProducts.find(item => item.itemId === parseInt(id));
}

// Function to reserve stock by item ID and stock
function reserveStockById(itemId, stock) {
    client.hset('item', `item.${itemId}`, stock);
}

// Function to get the current reserved stock by item ID (using Redis)
async function getCurrentReservedStockById(itemId) {
    const getAsync = util.promisify(client.hget).bind(client);
    return getAsync('item', `item.${itemId}`);
}

// Create an Express server
const app = express();

// Route to get the list of all products
app.get('/list_products', (req, res) => {
    res.json(listProducts).end();
});

// Route to get product details by item ID
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const product = getItemById(itemId);
    const reservedStock = await getCurrentReservedStockById(itemId);

    if (product) {
        product.currentQuantity = reservedStock !== null ? reservedStock : product.initialAvailableQuantity;
        res.json(product).end();
    } else {
        res.json({ status: 'Product not found' }).end();
    }
});

// Route to reserve a product by item ID
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const product = getItemById(itemId);

    if (product) {
        const reservedStock = await getCurrentReservedStockById(itemId) || product.initialAvailableQuantity;

        if (reservedStock > 0) {
            const newStock = reservedStock - 1;
            reserveStockById(itemId, newStock);
            res.json({ status: 'Reservation confirmed', itemId: itemId }).end();
        } else {
            res.json({ status: 'Not enough stock available', itemId: itemId }).end();
        }
    } else {
        res.json({ status: 'Product not found' }).end();
    }
});

// Start the server on port 1245
app.listen(1245, () => {
    console.log('Server is running on port 1245');
});
