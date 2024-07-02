import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css';
import ImageModal from './Modal';

const Gallery: React.FC = () => {
  const [images, setImages] = useState<string[]>([]);
  const [page, setPage] = useState(1);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [currentImage, setCurrentImage] = useState<string | null>(null);
  const [currentIndex, setCurrentIndex] = useState<number | null>(null);
  const imagesPerPage = 20;

  useEffect(() => {
    const fetchImages = async () => {
      const fetchedImages: string[] = [];
      for (let i = (page - 1) * imagesPerPage + 1; i <= page * imagesPerPage; i++) {
        fetchedImages.push(`http://localhost:8000/media/images/image_${i}.jpg`);
      }
      setImages(fetchedImages);
    };

    fetchImages();
  }, [page]);

  const openModal = (src: string, index: number) => {
    setCurrentImage(src);
    setCurrentIndex(index);
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
    setCurrentImage(null);
    setCurrentIndex(null);
  };

  const changeImage = async (id: number) => {
    if (currentIndex !== null) {
      try {
        console.log("Making PUT request...");
        const response = await axios.put(`http://localhost:8000/gallery/set_gallery_image/${currentIndex + 1}/`, {
          type: 'human',
          id: id,
        });
        console.log("Response data:", response.data);
        const updatedImage = `http://localhost:8000${response.data.image_url}`;
        const updatedImages = [...images];
        updatedImages[currentIndex] = updatedImage;
        setImages(updatedImages);
        console.log("Updated images array:", updatedImages);
        closeModal();
      } catch (error) {
        console.error("Error updating image:", error);
      }
    }
  };

  return (
    <div>
      <div className="gallery">
        {images.map((src, index) => (
          <img key={index} src={src} alt={`AI generated ${index}`} onClick={() => openModal(src, index)} />
        ))}
      </div>
      <div className="pagination">
        <button onClick={() => setPage(page - 1)} disabled={page === 1}>
          Previous
        </button>
        <button onClick={() => setPage(page + 1)}>
          Next
        </button>
      </div>
      <ImageModal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        imageUrl={currentImage}
        currentIndex={currentIndex}
        changeImage={changeImage}
      />
    </div>
  );
};

export default Gallery;
