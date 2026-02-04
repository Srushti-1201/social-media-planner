import { useEffect, useState } from "react";
import axios from "axios";
import { Container, Paper, Typography, Box, CircularProgress, Alert } from '@mui/material';

export default function ThirdParty() {
  const [quote, setQuote] = useState({ content: "", author: "" });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    axios.get("https://api.quotable.io/random")
      .then(res => setQuote(res.data))
      .catch(err => setError("Failed to fetch quote from the third-party API."))
      .finally(() => setLoading(false));
  }, []);

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Typography variant="h5" gutterBottom>Third-Party API Demo</Typography>
        <Typography variant="subtitle1" color="text.secondary" gutterBottom>Fetching data from api.quotable.io</Typography>
        {loading && <Box sx={{ display: 'flex', justifyContent: 'center', my: 3 }}><CircularProgress /></Box>}
        {error && <Alert severity="error" sx={{ my: 2 }}>{error}</Alert>}
        {quote.content && <Box sx={{ mt: 3, p: 2, borderLeft: '4px solid', borderColor: 'primary.main', bgcolor: 'grey.100' }}><Typography variant="h6" component="blockquote">"{quote.content}"</Typography><Typography variant="subtitle1" component="figcaption" align="right">— {quote.author}</Typography></Box>}
      </Paper>
    </Container>
  );
}